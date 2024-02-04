"""
Script for the CleaningClass
"""

# Import the required libraries
import pandas as pd
from sklearn.ensemble import IsolationForest

class DataCleaningClass:
    """
    Class for cleaning operations on a DataFrame
    """

    def __init__(self, df: pd.DataFrame):
        """
        Initialize the class with a DataFrame
        """
        self.df = df

    def remove_outliers(self, columns: list) -> pd.DataFrame:
        """
        Remove outliers from specified columns using Isolation Forest
        """
        # Handle missing values (drop rows with missing values)
        self.df = self.df.dropna(subset=columns)

        clf = IsolationForest(contamination=0.05)
        outliers_mask = clf.fit_predict(self.df[columns]) == -1
        self.df = self.df[~outliers_mask]
        return self.df

    def remove_duplicates(self) -> pd.DataFrame:
        """
        Remove duplicate rows from the DataFrame
        """
        self.df = self.df.drop_duplicates()
        return self.df

    def convert_to_lowercase(self) -> pd.DataFrame:
        """
        Convert all string columns to lowercase
        """
        self.df = self.df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
        return self.df

    def convert_first_letter_to_lowercase(self) -> pd.DataFrame:
        """
        Convert the first letter of all string columns to lowercase
        """
        self.df = self.df.applymap(lambda x: x[0].lower() + x[1:] if isinstance(x, str) else x)
        return self.df

    def min_age(self, min_age: int) -> pd.DataFrame:
        """
        Remove rows where 'age' is less than the specified
        """
        self.df = self.df[self.df['age'] >= min_age]
        return self.df

    def handle_missing_values(self) -> pd.DataFrame:
        """
        Handle missing values by dropping or imputing as needed
        """
        self.df = self.df.dropna()
        return self.df

    def age_columns(self):
        """
        Create a new column 'age_group' in the DataFrame based on age grouping in 10s.
        Ensure 'age' column is of integer type.
        """
        self.df["age"] = self.df["age"].astype(int)
        self.df["age_group"] = ((self.df["age"] // 10) * 10).astype(int)

    def remove_rows_with_other_gender(self) -> pd.DataFrame:
        """
        Remove rows where 'gender' column contains the value 'other'
        """
        self.df = self.df[self.df['gender'] != 'other']
        return self.df