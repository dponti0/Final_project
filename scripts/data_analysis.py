"""
Document for initial exploration of the Dataset
"""
# Import the needed libraries
import pandas as pd
import click
import matplotlib.pyplot as plt
import seaborn as sns
from .filtering import HotelDataFilter  # Import the filtering class


# Elaborate on the data analysis class
class HotelDataAnalysis:
    """
    Class for conducting data analysis on a Hotel Reservation DataFrame
    """

    def __init__(self, df: pd.DataFrame):
        """
        Initialize the class with a DataFrame
        """
        self.df = df

    def plot_cancellation_distribution(self):
        """
        Plot the distribution of cancellations
        """
        sns.countplot(x="is_canceled", data=self.df)
        plt.title("Distribution of Cancellations")
        plt.show()

    def plot_lead_time_distribution(self):
        """
        Plot the distribution of lead times
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df["lead_time"], bins=50, kde=True)
        plt.title("Distribution of Lead Times")
        plt.xlabel("Lead Time")
        plt.ylabel("Frequency")
        plt.show()

    def plot_reservations_per_hotel(self):
        """
        Plot the number of reservations for each hotel name
        """
        plt.figure(figsize=(12, 6))
        sns.countplot(
            x="hotel_name",
            data=self.df,
            order=self.df["hotel_name"].value_counts().index,
        )
        plt.title("Number of Reservations per Hotel")
        plt.xlabel("Hotel Name")
        plt.ylabel("Number of Reservations")
        plt.xticks(rotation=45, ha="right")
        plt.show()


def load_dataset(filename):
    """
    Function to load the dataset

    Parameters:
    - filename (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: Loaded DataFrame from the CSV file.
    """
    extension = filename.rsplit(".", 1)[-1]
    if extension.lower() != "csv":
        raise TypeError(f"The extension is {extension} and not 'csv'.")
    return pd.read_csv(filename)


@click.command()
@click.option("-i", "--input", help="Path to the CSV file", required=True)
def analyze_dataset(input):
    # Try & except (loading the dataset)
    try:
        df = load_dataset(input)
        print(f"The file '{input}' was correctly read!")

        # Create an instance of the filtering class
        filter_instance = HotelDataFilter(df)

        # Apply some filters (modify as needed)
        filtered_df = filter_instance.filter_cancel_status(canceled=False)

        # Create an instance of the analysis class
        analysis_instance = HotelDataAnalysis(filtered_df)

        # Perform data analysis
        analysis_instance.plot_cancellation_distribution()
        analysis_instance.plot_lead_time_distribution()
        analysis_instance.plot_reservations_per_hotel()

    except FileNotFoundError:
        print(f"Error: File not found at '{input}'. Provide a valid path")
    except pd.errors.EmptyDataError:
        print(f"Error: The file at '{input}' is empty")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    analyze_dataset()
