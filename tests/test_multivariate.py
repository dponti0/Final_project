"""
Script for testing the multivariate class
"""

# Import the necessary libraries
import unittest
from contextlib import redirect_stdout
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt
from scripts.multivariate_analysis import MultivariateVisualizer


class TestMultivariateVisualizer(unittest.TestCase):
    """
    Class that includes all the testing functions
    """

    def setUp(self):
        """
        Sample DataFrame for testing
        """
        data = {
            "age_cat": ["Teens", "Adults", "Elderly", "Teens", "Adults"],
            "stroke": [0, 1, 0, 1, 0],
            "avg_glucose_level": [80, 90, 100, 110, 120],
            "bmi": [22, 25, 30, 28, 26],
            "gender": ["Male", "Female", "Male", "Female", "Male"],
            "heart_disease": [0, 1, 0, 1, 0],
            "smoking_status": [
                "Non-smoker",
                "Smoker",
                "Non-smoker",
                "Unknown",
                "Unknown",
            ],
            "ever_married": ["Yes", "Yes", "No", "Yes", "No"],
            "work_type": [
                "Private",
                "Govt",
                "Private",
                "Self-employed",
                "Self-employed",
            ],
        }
        self.df = pd.DataFrame(data)
        self.visualizer = MultivariateVisualizer(self.df)

    def test_age_stroke_distribution(self):
        """
        Test the age-stroke distribution visualization
        """
        self._test_visualization_method(self.visualizer.age_stroke_distribution)

    def test_glucose_stroke_distribution(self):
        """
        Test the glucose-stroke visualization function
        """
        self._test_visualization_method(self.visualizer.glucose_stroke_distribution)

    def test_bmi_stroke_distribution(self):
        """
        Test the bmi-stroke visualization function
        """
        self._test_visualization_method(self.visualizer.bmi_stroke_distribution)

    def test_bmi_glucose_scatter(self):
        """
        Test the bmi-glucose visualization function
        """               
        self._test_visualization_method(self.visualizer.bmi_glucose_scatter)

    def test_glucose_smoking_distribution(self):
        """
        Test the glucose-smoking status function
        """
        self._test_visualization_method(self.visualizer.glucose_smoking_distribution)

    def test_work_type_stroke_distribution(self):
        """
        Test the strokes related to work type function
        """
        self._test_visualization_method(self.visualizer.work_type_stroke_distribution)

    def test_marriage_glucose_relation(self):
        """
        Test the relation between marriage and bmi function
        """
        self._test_visualization_method(self.visualizer.marriage_glucose_relation)

    def test_age_stroke_rate_lineplot(self):
        """
        Test the lineplot visualization function
        """    
        self._test_visualization_method(self.visualizer.age_stroke_rate_lineplot)

    def test_marriage_bmi_relation(self):
        """
        Test the marriage-bmi relation function
        """
        self._test_visualization_method(self.visualizer.marriage_bmi_relation)

    def test_correlation_heatmap(self):
        """
        Test the correlation heatmap 
        """
        self._test_visualization_method(self.visualizer.correlation_heatmap)

    def _test_visualization_method(self, method):
        """
        Test the given visualization method
        """
        # Redirect stdout to capture the plot output
        with redirect_stdout(BytesIO()):
            method()

        # Check if any of the dimensions are zero
        plt_dims = plt.gcf().get_size_inches()
        self.assertFalse(
            any(dim == 0 for dim in plt_dims),
            f"Plot dimensions should not be zero. Method: {method.__name__}",
        )

        # Close the plot to avoid overlapping plots
        plt.close()


if __name__ == "__main__":
    unittest.main()
