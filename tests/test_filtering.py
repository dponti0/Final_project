"""
Script for testing the filtering class
"""

import unittest
import pandas as pd


class FilteringClass:
    """
    Dummy class for testing purposes.
    """

    def __init__(self, df):
        self.df = df

    def filter_by_hypertension(self):
        return self.df[self.df["hypertension"] == 1]

    def filter_by_heart_disease(self):
        return self.df[self.df["heart_disease"] == 1]

    def filter_by_high_glucose(self, threshold):
        return self.df[self.df["avg_glucose_level"] > threshold]

    def filter_by_high_bmi(self, threshold):
        return self.df[self.df["bmi"] > threshold]

    def filter_by_stroke(self):
        return self.df[self.df["stroke"] == 1]


class TestFilteringClass(unittest.TestCase):
    """
    Class for testing the FilteringClass methods.
    """

    def setUp(self):
        """
        Set up a sample DataFrame for testing.
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
        """
        Test the filter_by_hypertension method.
        All individuals should have hypertension.
        """
        filtered_df = self.filtering_instance.filter_by_hypertension()
        self.assertEqual(
            filtered_df["hypertension"].sum(),
            len(filtered_df),
            "All individuals should have hypertension.",
        )

    def test_filter_by_heart_disease(self):
        """
        Test the filter_by_heart_disease method.
        All individuals should have heart disease.
        """
        filtered_df = self.filtering_instance.filter_by_heart_disease()
        self.assertEqual(
            filtered_df["heart_disease"].sum(),
            len(filtered_df),
            "All individuals should have heart disease.",
        )

    def test_filter_by_high_glucose(self):
        """
        Test the filter_by_high_glucose method.
        All individuals should have high glucose levels.
        """
        glucose_threshold = 150
        filtered_df = self.filtering_instance.filter_by_high_glucose(glucose_threshold)
        self.assertTrue(
            all(filtered_df["avg_glucose_level"] > glucose_threshold),
            "All individuals should have high glucose levels.",
        )

    def test_filter_by_high_bmi(self):
        """
        Test the filter_by_high_bmi method.
        All individuals should have high BMI.
        """
        bmi_threshold = 30
        filtered_df = self.filtering_instance.filter_by_high_bmi(bmi_threshold)
        self.assertTrue(
            all(filtered_df["bmi"] > bmi_threshold),
            "All individuals should have high BMI.",
        )

    def test_filter_by_stroke(self):
        """
        Test the filter_by_stroke method.
        All individuals should have had a stroke.
        """
        filtered_df = self.filtering_instance.filter_by_stroke()
        self.assertEqual(
            filtered_df["stroke"].sum(),
            len(filtered_df),
            "All individuals should have had a stroke.",
        )


if __name__ == "__main__":
    unittest.main()
