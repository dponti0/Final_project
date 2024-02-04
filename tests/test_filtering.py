"""
Script for testing the filtering class
"""

# Import the necessary libraries
import unittest
import pandas as pd
from scripts.filtering import FilteringClass


class TestFilteringClass(unittest.TestCase):
    """
    Class that includes all the testing functions
    """

    def setUp(self):
        """
        Sample DataFrame for testing
        """
        data = {
            "hypertension": [0, 1, 0, 1, 0],
            "heart_disease": [1, 0, 1, 0, 1],
            "avg_glucose_level": [120, 130, 140, 160, 170],
            "bmi": [25, 28, 30, 32, 29],
            "stroke": [0, 1, 0, 1, 0],
        }
        self.df = pd.DataFrame(data)
        self.filtering_instance = FilteringClass(self.df)

    def test_filter_by_hypertension(self):
        filtered_df = self.filtering_instance.filter_by_hypertension()
        self.assertEqual(
            filtered_df["hypertension"].sum(),
            len(filtered_df),
            "All individuals should have hypertension.",
        )

    def test_filter_by_heart_disease(self):
        filtered_df = self.filtering_instance.filter_by_heart_disease()
        self.assertEqual(
            filtered_df["heart_disease"].sum(),
            len(filtered_df),
            "All individuals should have heart disease.",
        )

    def test_filter_by_high_glucose(self):
        glucose_threshold = 150
        filtered_df = self.filtering_instance.filter_by_high_glucose(glucose_threshold)
        self.assertTrue(
            all(filtered_df["avg_glucose_level"] > glucose_threshold),
            "All individuals should have high glucose levels.",
        )

    def test_filter_by_high_bmi(self):
        bmi_threshold = 30
        filtered_df = self.filtering_instance.filter_by_high_bmi(bmi_threshold)
        self.assertTrue(
            all(filtered_df["bmi"] > bmi_threshold),
            "All individuals should have high BMI.",
        )

    def test_filter_by_stroke(self):
        filtered_df = self.filtering_instance.filter_by_stroke()
        self.assertEqual(
            filtered_df["stroke"].sum(),
            len(filtered_df),
            "All individuals should have had a stroke.",
        )


if __name__ == "__main__":
    unittest.main()
