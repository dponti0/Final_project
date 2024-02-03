import os
import pandas as pd
import click
from cleaning_class import DataCleaningClass  

# Click command
@click.command(short_help="Clean and filter dataset")
@click.option(
    "-i",
    "--input",
    default="dataset/healthcare_dataset.csv",
    required=True,
    help="Input CSV file path",
)
@click.option(
    "-o",
    "--output",
    default="outputs/cleaned_dataset.csv",
    help="Output CSV file path",
)
def main_function(input, output):
    """
    Main function to load, clean & filter the dataset
    """
    try:
        extension = input.rsplit(".", 1)[-1]
        if extension.lower() != "csv":
            raise TypeError(
                f"The extension is {extension} and not 'csv'. Please provide a CSV file."
            )

        # Load the dataset
        health_data = pd.read_csv(input)

        # Print the shape of the original dataset
        print("Original dataset shape:", health_data.shape)

        # Initialize the cleaning class
        cleaning_instance = DataCleaningClass(health_data)

        # Convert the first letter of all string columns to lowercase
        cleaning_instance.convert_first_letter_to_lowercase()

        # Remove outliers from specific columns
        columns_with_outliers = ["age", "avg_glucose_level", "bmi"]
        cleaned_data = cleaning_instance.remove_outliers(columns_with_outliers)

        # Remove duplicates
        cleaned_data = cleaning_instance.remove_duplicates()

        # Remove rows where 'age' is less than 10
        cleaned_data = cleaning_instance.min_age(10)

        # Handle missing values
        cleaned_data = cleaning_instance.handle_missing_values()

        # Create a new column 'age_group' based on age grouping in 10s
        cleaning_instance.age_columns()

        # Crear la columna 'age_cat'
        bins = [0, 12, 18, 35, 60, float('inf')]
        labels = ['Children', 'Teens', 'Adults', 'Mid Adults', 'Elderly']

        cleaned_data['age_cat'] = pd.cut(cleaned_data['age'], bins=bins, labels=labels, right=False)

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
        os.makedirs(
            os.path.dirname(output), exist_ok=True
        )  # Create the output folder if it doesn't exist
        cleaned_data.to_csv(output, index=False)
        print(f"The cleaned version of the dataset was saved to {output}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    print("The code is properly working!")
    main_function()

# python scripts/data_cleaning.py -i dataset/healthcare_dataset.csv -o outputs/cleaned_dataset.csv
