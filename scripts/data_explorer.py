# dataset_explorer.py

import os
import pandas as pd

class DatasetExplorer:
    """
    A class for exploring and analyzing datasets.
    """

    def __init__(self, df):
        """
        Initialize the DatasetExplorer with a DataFrame.
        """
        self.df = df
        self.output_file = os.path.join("outputs", "exploration_output.txt")
        print()  

    def save_to_file(self, content):
        """
        Save content to a text file.
        """
        with open(self.output_file, 'a') as file:
            file.write(content + "\n\n")

    def display_info(self):
        """
        Display basic information about the dataset, including data types and non-null counts.
        """
        content = "Basic information about the dataset:\n\n"
        content += str(self.df.info())
        self.save_to_file(content)
        print(content)

    def display_head(self, n=5):
        """
        Display the first 'n' rows of the dataset.
        """
        content = f"Displaying the first {n} rows of the dataset:\n\n"
        content += str(self.df.head(n))
        self.save_to_file(content)
        print(content)

    def display_descriptive_stats(self):
        """
        Display descriptive statistics of numerical columns in the dataset.
        """
        content = "Descriptive statistics of the numerical columns:\n\n"
        num_col = self.df.select_dtypes(include=['number']).columns
        content += str(self.df[num_col].describe())
        self.save_to_file(content)
        print(content)

    def display_missing_values_sum(self):
        """
        Display the sum of missing values for each column in the dataset.
        """
        content = "Sum of missing values for each column:\n\n"
        content += str(self.df.isna().sum())
        self.save_to_file(content)
        print(content)

    def display_unique_values(self, columns):
        """
        Display unique values for specified columns in the dataset.
        """
        content = "Unique values for specified columns:\n\n"
        for column in columns:
            unique_values = self.df[column].unique()
            content += f"{column}: {unique_values}\n"
        self.save_to_file(content)
        print(content)

    def display_value_counts(self):
        """
        Display value counts for categorical columns in the dataset.
        """
        content = "Value counts for categorical columns:\n\n"
        cat_columns = self.df.select_dtypes(include=['object']).columns
        for column in cat_columns:
            value_counts = self.df[column].value_counts()
            content += f"{column}:\n{value_counts}\n\n"
        self.save_to_file(content)
        print(content)

    def display_correlation_matrix(self):
        """
        Display the correlation matrix for numerical columns in the dataset.
        """
        content = "Correlation matrix for numerical columns:\n\n"
        num_col = self.df.select_dtypes(include=['number']).columns
        correlation_matrix = self.df[num_col].corr()
        content += str(correlation_matrix)
        self.save_to_file(content)
        print(content)