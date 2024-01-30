# initial_exploration.py

import os
import pandas as pd
from data_explorer import DatasetExplorer  # Import the DatasetExplorer class

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

        # Display unique values for specified columns
        specified_columns = ["smoking_status", "gender", "work_type", "Residence_type"]
        explorer.display_unique_values(specified_columns)

        # Display value counts for categorical columns
        explorer.display_value_counts()

        # Display correlation matrix for numerical columns
        explorer.display_correlation_matrix()

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    print("The initial exploration is about to launch!!")
    # Create or clear the exploration output file
    with open(os.path.join("outputs", "exploration_output.txt"), 'w'):
        pass
    explore_dataset()
