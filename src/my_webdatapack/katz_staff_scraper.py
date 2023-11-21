import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

class KatzStaffScraper:
    def __init__(self, url):
        self.url = url
        self.soup = None
        self.staff_info = None

    def fetch_page_content(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.content, 'html.parser')
        else:
            raise ConnectionError(f"Failed to fetch page content, status code: {response.status_code}")

    def parse_html(self):
        self.staff_info = self.soup.find_all('div', class_='text-only')

    def extract_staff_details(self):
        # Extract Names
        names = []
        for name in self.staff_info[0].find_all('p'):
            name = name.get_text()
            name = name.split('\xa0\n\xa0\n')
            if len(name) == 1:
                name = name[0].split(',')
                names.append(name[0])
            else:
                for n in name:
                    n = n.split(',')
                    names.append(n[0])
        names = list(filter(lambda x: len(x) > 0 and x != '\xa0', names))

        # Extract Emails
        emails = []
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        for email in self.staff_info[0].find_all('p'):
            for a in email.find_all('a'):
                emails.append(a.text)
        emails = list(filter(lambda x: 'Schedule an Appointment' not in x, emails))
        emails = list(map(lambda x: x if re.match(email_pattern, x) else 'NA', emails))

        # Extract Titles
        titles = []
        i = 0
        for title in self.staff_info[0].find_all('p'):
            title = title.get_text()
            title = title.split('\xa0\n\xa0\n')
            if title == ['\xa0']:
                continue
            if len(title) == 1:
                titles.append(title[0].split(',')[1].split(emails[i])[0])
                i += 1
            else:
                for t in title:
                    titles.append(t.split(',')[1].split(emails[i])[0])
                    i += 1

        # Extract Offices
        h3_elements = self.staff_info[0].find_all('h3')
        offices = [h3.get_text().strip() for h3 in h3_elements]

        # Extract Phone Numbers
        phone_nums = []
        phone_pattern = r'(\+\d{1,3}\s?)?(\d{3}[-\s]?\d{3}[-\s]?\d{4})'
        i = 0
        for phones in self.staff_info[0].find_all('p'):
            phones = phones.get_text()
            phones = phones.split('\xa0\n\xa0\n')
            if phones == ['\xa0']:
                continue
            if len(phones) == 1:
                filter_phone = re.findall(phone_pattern, phones[0])
                if filter_phone:
                    phone_nums.append(filter_phone[0][1])
                else:
                    phone_nums.append("NA")
                i += 1
            else:
                for p in phones:
                    filter_phone = re.findall(phone_pattern, p)
                    if filter_phone:
                        phone_nums.append(filter_phone[0][1])
                    else:
                        phone_nums.append("NA")
                    i += 1

        return names, titles, emails, phone_nums, offices

    def create_dataframe(self, names, titles, emails, phone_nums, offices):
        staff_df = pd.DataFrame({
            "name": names,
            "title": titles,
            "email": emails,
            "phone": phone_nums
        })

        # Assigning office values
        staff_df['office'] = ''
        staff_df.loc[:6, 'office'] = offices[0]
        staff_df.loc[7:11, 'office'] = offices[1]
        staff_df.loc[12, 'office'] = offices[2]
        staff_df.loc[13:, 'office'] = offices[3]

        return staff_df

# module usage (to be demonstrated in a Jupyter Notebook)
# url = "https://www.yu.edu/katz/staff"
# scraper = KatzStaffScraper(url)
# scraper.fetch_page_content()
# scraper.parse_html()
# names, titles, emails, phone_nums, offices = scraper.extract_staff_details()
# staff_df = scraper.create_dataframe(names, titles, emails, phone_nums, offices)
# staff_df.head()  # Show first few rows of the DataFrame


