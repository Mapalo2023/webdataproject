import pandas as pd

class KatzStaffAnalysis(df):
    """
    A class for analyzing staff data from the Katz School.

    Attributes:
    df (pandas.DataFrame): A DataFrame containing staff information.
    """

    def title_distribution(df):
        """
        Calculate the distribution of staff titles.

        Parameters:
        df (pandas.DataFrame): The DataFrame containing staff information.
 
        Returns:
        pandas.Series: A series containing counts of each unique title.
        """
        return df['title'].value_counts()

    def email_domain_analysis(df):
        """
        Analyze the distribution of email domains among the staff.

        Parameters:
        df (pandas.DataFrame): The DataFrame containing staff information.

        Returns:
        pandas.Series: A series containing counts of each unique email domain.
        """
        df['email_domain'] = df['email'].apply(lambda x: x.split('@')[-1] if '@' in x else None)
        return df['email_domain'].value_counts()

    def phone_number_availability(df):
        """
        Determine the availability of phone numbers for staff members.

        Parameters:
        df (pandas.DataFrame): The DataFrame containing staff information.

        Returns:
        pandas.Series: A series indicating the count of staff with and without phone numbers.
        """
        has_phone = df['phone'].apply(lambda x: 'Yes' if x != 'NA' else 'No')
        return has_phone.value_counts()

    def office_staff_count(df):
        """
        Count the number of staff members in each office.

        Parameters:
        df (pandas.DataFrame): The DataFrame containing staff information.

        Returns:
        pandas.Series: A series containing counts of staff in each office.
        """
        return df['office'].value_counts()
