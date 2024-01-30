"""
Script for cleaning the DataFrame
"""

import os
import pandas as pd
import click
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
        # Handle missing values (drop rows with missing values for simplicity, adjust as needed)
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

    def handle_missing_values(self) -> pd.DataFrame:
        """
        Handle missing values by dropping or imputing as needed
        """
        self.df = self.df.dropna()
        return self.df
    
    def create_age_group_column(self):
        """
        Create a new column 'age_group' in the DataFrame based on age grouping in 10s.
        """
        self.df['age_group'] = ((self.df['age'] // 10) * 10).astype(int)

# Click command
@click.command(short_help="Clean and filter dataset")
@click.option("-i", "--input", default="healthcare_dataset.csv", required=True, help="Input CSV file path")
@click.option("-o", "--output", default="cleaned_healthcare_dataset.csv", help="Output CSV file path")

def main_function(input, output):
    """
    Main function to load, clean & filter the dataset
    """
    try:
        extension = input.rsplit(".", 1)[-1]
        if extension.lower() != "csv":
            raise TypeError(f"The extension is {extension} and not 'csv'. Please provide a CSV file.")
        
        # Load the dataset
        health_data = pd.read_csv(input)

        # Print the shape of the original dataset
        print("Original dataset shape:", health_data.shape)

        # Initialize the cleaning class
        cleaning_instance = DataCleaningClass(health_data)

        # Remove outliers from specific columns
        columns_with_outliers = ['age', 'avg_glucose_level', 'bmi']
        cleaned_data = cleaning_instance.remove_outliers(columns_with_outliers)

        # Remove duplicates
        cleaned_data = cleaning_instance.remove_duplicates()

        # Handle missing values
        cleaned_data = cleaning_instance.handle_missing_values()

        # Create a new column 'age_group' based on age grouping in 10s
        cleaning_instance.create_age_group_column()

        # Print the shape of the cleaned dataset
        print("Cleaned dataset shape:", cleaned_data.shape)

        # Check if the cleaned dataset has any missing values
        if cleaned_data.isnull().values.any():
            print("The cleaned dataset contains missing values")
        else:
            print("The cleaned dataset has no missing values")

        # Check if the cleaned dataset has any duplicates
        if cleaned_data.duplicated().any():
            print("The cleaned dataset contains duplicates")
        else:
            print("The cleaned dataset has no duplicates either")

        # Save the cleaned and filtered dataset to the specified output file
        os.makedirs(os.path.dirname(output), exist_ok=True)     # Create the output folder if it doesn't exist
        cleaned_data.to_csv(output, index=False)
        print(f"The cleaned version of the dataset was saved to {output}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    print("The code is properly working!")
    main_function()

# python scripts/data_cleaning.py -i dataset/healthcare_dataset.csv -o outputs/cleaned_dataset.csv
    