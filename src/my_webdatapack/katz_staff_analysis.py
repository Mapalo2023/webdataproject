import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
        Calculates the distribution of staff titles.

        Parameters:
        df (pandas.DataFrame): The DataFrame containing staff information.
 
        Returns:
        pandas.Series: A series containing counts of each unique title.
        """
        return self.df['title'].value_counts()

    def email_domain_analysis(self):
        """
        Analyzes the distribution of email domains among the staff.

        Parameters:
        df (pandas.DataFrame): The DataFrame containing staff information.

        Returns:
        pandas.Series: A series containing counts of each unique email domain.
        """
        self.df['email_domain'] = self.df['email'].apply(lambda x: x.split('@')[-1] if '@' in x else None)
        return self.df['email_domain'].value_counts()

    def phone_number_availability(self):
        """
        Determines the availability of phone numbers for staff members.

        Parameters:
        df (pandas.DataFrame): The DataFrame containing staff information.

        Returns:
        pandas.Series: A series indicating the count of staff with and without phone numbers.
        """
        has_phone = self.df['phone'].apply(lambda x: 'Yes' if x != 'NA' else 'No')
        return has_phone.value_counts()

    def office_staff_count(self):
        """
        Counts the number of staff members in each office.

        Parameters:
        df (pandas.DataFrame): The DataFrame containing staff information.

        Returns:
        pandas.Series: A series containing counts of staff in each office.
        """
        return self.df['office'].value_counts()


    def plot_title_distribution(self):
        """
        Creates a histogram for the distribution of staff titles.

        This function creates a histogram that shows the frequency of each unique staff title.
        """
        title_counts = self.df['title'].value_counts()
        plt.figure(figsize=(10, 6))
        sns.barplot(x=title_counts.values, y=title_counts.index, palette='BuGn', alpha=0.8)
        plt.xlabel('Count')
        plt.ylabel('Title')
        plt.title('Distribution of Staff Titles')
        plt.show()

    def plot_email_domain_distribution(self):
        """
        Creates a bar plot for the distribution of email domains.

        This function creates a bar plot that shows the frequency of each unique email domain.
        """
        self.df['email_domain'] = self.df['email'].apply(lambda x: x.split('@')[-1] if '@' in x else None)
        domain_counts = self.df['email_domain'].value_counts()
        plt.figure(figsize=(8, 4))
        sns.barplot(x=domain_counts.index, y=domain_counts.values, palette='mako', alpha=0.8)
        plt.xlabel('Email Domain')
        plt.ylabel('Count')
        plt.title('Email Domain Distribution')
        plt.show()

    def phone_vs_office_scatter(self):
        """
        Creates a scatter plot to visualize the relationship between phone number availability and office location.

        This function creates a scatter plot showing the distribution of staff members who have or don't have phone numbers across different offices.
        """
        has_phone = self.df['phone'].apply(lambda x: 1 if x != 'NA' else 0)
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=self.df['office'], y=has_phone, alpha=0.7)
        plt.xlabel('Office')
        plt.ylabel('Has Phone (1: Yes, 0: No)')
        plt.title('Phone Availability vs Office')
        plt.xticks(rotation=45)
        plt.show()

  