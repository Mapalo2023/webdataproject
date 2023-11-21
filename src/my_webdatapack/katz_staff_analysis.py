import pandas as pd

class KatzStaffAnalysis:
    """
    A class for analyzing staff data from the Katz School.

    Attributes:
    df (pandas.DataFrame): A DataFrame containing staff information.
    """
    def __init__(self, df):
        self.df = df

    def title_distribution(self):
        """
        Calculate the distribution of staff titles.

        Parameters:
        df (pandas.DataFrame): The DataFrame containing staff information.
 
        Returns:
        pandas.Series: A series containing counts of each unique title.
        """
        return self.df['title'].value_counts()

    def email_domain_analysis(self):
        """
        Analyze the distribution of email domains among the staff.

        Parameters:
        df (pandas.DataFrame): The DataFrame containing staff information.

        Returns:
        pandas.Series: A series containing counts of each unique email domain.
        """
        self.df['email_domain'] = self.df['email'].apply(lambda x: x.split('@')[-1] if '@' in x else None)
        return self.df['email_domain'].value_counts()

    def phone_number_availability(self):
        """
        Determine the availability of phone numbers for staff members.

        Parameters:
        df (pandas.DataFrame): The DataFrame containing staff information.

        Returns:
        pandas.Series: A series indicating the count of staff with and without phone numbers.
        """
        has_phone = self.df['phone'].apply(lambda x: 'Yes' if x != 'NA' else 'No')
        return has_phone.value_counts()

    def office_staff_count(self):
        """
        Count the number of staff members in each office.

        Parameters:
        df (pandas.DataFrame): The DataFrame containing staff information.

        Returns:
        pandas.Series: A series containing counts of staff in each office.
        """
        return self.df['office'].value_counts()
