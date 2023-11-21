import requests
import pandas as pd
import xml.etree.ElementTree as ET

class ForbesSitemapParser:
    """
    A parser for fetching and parsing sitemap data from Forbes' website.

    Attributes:
        base_url (str): Base URL of the Forbes website.
        sitemap_urls (list): List of URLs to sitemaps found in the robots.txt file.
    """

    def __init__(self):
        """Initialize the parser with the base URL and an empty list for sitemap URLs."""
        self.base_url = 'https://www.forbes.com'
        self.sitemap_urls = []

    def fetch_robots_txt(self):
        """
        Fetch the robots.txt file from the Forbes website.

        Returns:
            str: The content of the robots.txt file, or None if there was an error.
        """
        try:
            response = requests.get(f'{self.base_url}/robots.txt')
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching robots.txt: {e}")
            return None

    def parse_robots_txt(self, robots_txt):
        """
        Parse the robots.txt file to find sitemap URLs.

        Args:
            robots_txt (str): Content of the robots.txt file.
        """
        for line in robots_txt.splitlines():
            if line.startswith('Sitemap:'):
                sitemap_url = line.split(': ')[1]
                self.sitemap_urls.append(sitemap_url)

    def fetch_sitemap(self, url):
        """
        Fetch a sitemap from a given URL.

        Args:
            url (str): The URL of the sitemap to fetch.

        Returns:
            bytes: The content of the sitemap, or None if there was an error.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.content
        except requests.RequestException as e:
            print(f"Error fetching sitemap: {e}")
            return None

    def parse_sitemap(self, sitemap_xml):
        """
        Parse the XML content of a sitemap to extract URLs.

        Args:
            sitemap_xml (str): XML content of a sitemap.

        Returns:
            list: A list of URLs found in the sitemap.
        """
        root = ET.fromstring(sitemap_xml)
        urls = []
        for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
            loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
            urls.append(loc)
        return urls

    def get_sitemap_data(self):
        """
        Retrieve and parse sitemap data from the Forbes website.

        Returns:
            DataFrame: A pandas DataFrame containing URLs from the sitemaps.
        """
        robots_txt = self.fetch_robots_txt()
        if robots_txt:
            self.parse_robots_txt(robots_txt)
            all_urls = []
            for sitemap_url in self.sitemap_urls:
                sitemap_xml = self.fetch_sitemap(sitemap_url)
                if sitemap_xml:
                    urls = self.parse_sitemap(sitemap_xml)
                    all_urls.extend(urls)
            return pd.DataFrame({'urls': all_urls})


