# explore_dataset.py

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
        print()  

    def display_info(self):
        """
        Display basic information about the dataset, including data types and non-null counts.
        """
        print("Basic information about the dataset:")
        print()
        print(self.df.info())
        print()  # Adding empty lines to better visualize the data

    def display_head(self, n=5):
        """
        Display the first 'n' rows of the dataset.
        """
        print(f"Displaying the first {n} rows of the dataset:")
        print(self.df.head(n))
        print()

    def display_descriptive_stats(self):
        """
        Display descriptive statistics of numerical columns in the dataset.
        """
        print("Descriptive statistics of the numerical columns:")
        num_col = self.df.select_dtypes(include=['number']).columns
        print(self.df[num_col].describe())
        print()

    def display_missing_values_sum(self):
        """
        Display the sum of missing values for each column in the dataset.
        """
        print("Sum of missing values for each column:")
        print(self.df.isna().sum())
        print()

def explore_dataset(input_path="dataset/healthcare_dataset.csv"):
    """
    Main function to explore the dataset.
    """
    try:
        # Load the dataset
        dataset = pd.read_csv(input_path)

        # Initialize the DatasetExplorer class
        explorer = DatasetExplorer(dataset)

        # Display basic information about the dataset
        explorer.display_info()

        # Display the first 5 rows of the dataset
        explorer.display_head()

        # Display descriptive statistics
        explorer.display_descriptive_stats()

        # Display the sum of missing values for each column
        explorer.display_missing_values_sum()

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    print("The initial exploration is about to launch!!")
    explore_dataset()

    # python scripts/initial_exploration.py