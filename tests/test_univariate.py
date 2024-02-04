"""
Script for testing the univariate class
"""

# Import the necessary libraries
import unittest
from contextlib import redirect_stdout
from io import BytesIO
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scripts.univariate_analysis import UnivariateVisualizer


class TestUnivariateVisualizer(unittest.TestCase):
    """
    Class that includes all the testing functions
    """

    def setUp(self):
        """
        Sample DataFrame for testing
        """
        data = {
            "age": [25, 35, 45, 55, 65],
            "age_group": [20, 30, 40, 50, 60],
            "gender": ["Male", "Female", "Male", "Female", "Male"],
            "hypertension": [0, 1, 1, 0, 1],
            "heart_disease": [0, 1, 0, 1, 0],
            "avg_glucose_level": [80, 90, 100, 110, 120],
            "bmi": [22, 25, 30, 28, 26],
            "work_type": [
                "Private",
                "Govt",
                "Private",
                "Self-employed",
                "Self-employed",
            ],
            "ever_married": ["Yes", "Yes", "No", "Yes", "No"],
            "Residence_type": ["Urban", "Urban", "Rural", "Urban", "Rural"],
            "smoking_status": [
                "Non-smoker",
                "Smoker",
                "Non-smoker",
                "Unknown",
                "Unknown",
            ],
            "stroke": [0, 1, 0, 1, 0],
        }
        self.df = pd.DataFrame(data)
        self.visualizer = UnivariateVisualizer(self.df)

    def test_visualize_age_distribution(self):
        """
        Test visualization of age distribution
        """
        self._test_visualization_method(self.visualizer.visualize_age_distribution)

    def test_visualize_age_group_distribution(self):
        """
        Test the visualization of the age group column distribution
        """
        self._test_visualization_method(
            self.visualizer.visualize_age_group_distribution
        )

    def visualize_gender_distribution(self):
        """
        Test the visualization of the gender distribution in the dataset
        """
        f_df = self.df[self.df["gender"].isin(["male", "female"])]
        gender_percentages = f_df["gender"].value_counts(normalize=True) * 100

        # Check if gender_percentages.values is not empty
        if not gender_percentages.empty:
            sns.set(style="whitegrid")
            plt.figure(figsize=(7, 5))
            _ = sns.barplot(
                x=gender_percentages.values,
                y=gender_percentages.index,
                palette="pastel",
            )
            plt.title("Gender Distribution", weight="bold")
            plt.ylabel("Gender", fontstyle="italic", fontsize=9)
            plt.xticks([])
            sns.despine(bottom=True)
            self.save_and_close()
        else:
            print("No gender data available for visualization")

    def test_visualize_hypertension_distribution(self):
        """
        Test the visualization of the hypertension distribution
        """
        self._test_visualization_method(
            self.visualizer.visualize_hypertension_distribution
        )

    def test_visualize_heart_disease_distribution(self):
        """
        Test the visualization of the heart disease distribution in the dataset
        """
        self._test_visualization_method(
            self.visualizer.visualize_heart_disease_distribution
        )

    def test_visualize_glucose_distribution(self):
        """
        Test the visualization of the average glucose level distribution in the dataset
        """
        self._test_visualization_method(self.visualizer.visualize_glucose_distribution)

    def test_visualize_bmi_distribution(self):
        """
        Test the visualization of the bmi distribution in the dataset
        """
        self._test_visualization_method(self.visualizer.visualize_bmi_distribution)

    def test_visualize_work_type_distribution(self):
        """
        Test the visualization of the work type distribution in the dataset
        """
        self._test_visualization_method(
            self.visualizer.visualize_work_type_distribution
        )

    def test_visualize_marital_status_distribution(self):
        """
        Test the visualization of the marital status distribution of the dataset
        """
        self._test_visualization_method(
            self.visualizer.visualize_marital_status_distribution
        )

    def test_visualize_residence_type_distribution(self):
        """
        Test the visualization of the residence type distribution
        """
        self._test_visualization_method(
            self.visualizer.visualize_residence_type_distribution
        )

    def test_visualize_smoking_distribution(self):
        """
        Test the visualization the smoking column distribution of the dataset
        """
        self._test_visualization_method(self.visualizer.visualize_smoking_distribution)

    def test_visualize_strokes_distribution(self):
        """
        Test the visualization of the strokes distribution in the dataset
        """
        self._test_visualization_method(self.visualizer.visualize_strokes_distribution)

    def _test_visualization_method(self, method):
        """
        Test the given visualization method
        """
        # Redirect stdout to capture the plot output
        with redirect_stdout(BytesIO()):
            method()

        # Check if any of the dimensions are zero
        self.assertFalse(any(dim == 0 for dim in plt.gcf().get_size_inches()))

        # Close the plot to avoid overlapping plots
        plt.close()


if __name__ == "__main__":
    unittest.main()
