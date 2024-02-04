"""
Script for testing the cleaning class
"""

# Import the necessary libraries
import unittest
from unittest.mock import patch
import pandas as pd
from scripts.cleaning_class import DataCleaningClass


class TestDataCleaningClass(unittest.TestCase):
    """
    Class that includes all the testing functions
    """

    def setUp(self):
        # Sample data for testing
        data = {
            "age": [25, 30, 40, 45, 50, 60, 70, 80, 90, 100],
            "gender": [
                "Male",
                "Female",
                "Male",
                "Female",
                "Male",
                "Female",
                "Male",
                "Female",
                "Male",
                "Female",
            ],
        }
        self.df = pd.DataFrame(data)
        self.cleaning_instance = DataCleaningClass(self.df.copy())

    def test_remove_outliers(self):
        """
        Testing the remove outliers function
        """
        with patch(
            "sklearn.ensemble.IsolationForest", return_value=MockIsolationForest()
        ):
            cleaned_data = self.cleaning_instance.remove_outliers(["age"])
        self.assertFalse(any(cleaned_data["age"] > 100))

    def test_remove_duplicates(self):
        """
        Testing the remove duplicates function
        """
        # Create a duplicate row
        duplicate_row = pd.DataFrame({"age": [25], "gender": ["Male"]})
        self.df = pd.concat([self.df, duplicate_row], ignore_index=True)

        cleaned_data = self.cleaning_instance.remove_duplicates()
        self.assertEqual(len(cleaned_data), len(self.df.drop_duplicates()))

    def test_convert_first_letter_to_lowercase(self):
        """
        Testing the converting to lowercase the first letter function
        """
        self.df["gender"] = self.df["gender"].apply(lambda x: x.upper())
        cleaned_data = self.cleaning_instance.convert_first_letter_to_lowercase()
        self.assertTrue(all(cleaned_data["gender"].str.islower()))

    def test_min_age(self):
        """
        Testing the minimum age function
        """
        cleaned_data = self.cleaning_instance.min_age(40)
        self.assertTrue(all(cleaned_data["age"] >= 40))

    def test_handle_missing_values(self):
        """
        Testing the missing values function
        """
        self.df.loc[1, "age"] = None
        cleaned_data = self.cleaning_instance.handle_missing_values()
        self.assertFalse(cleaned_data["age"].isnull().any())

    def test_age_columns(self):
        """
        Testing the cleaning the age column function
        """
        self.cleaning_instance.age_columns()
        self.assertTrue("age_group" in self.cleaning_instance.df.columns)

    def test_remove_rows_with_other_gender(self):
        """
        Testing the function that remove the rows with "others" as gender
        """
        # Create a row with 'Other' gender
        other_gender_row = pd.DataFrame({"age": [35], "gender": ["Other"]})
        self.df = pd.concat([self.df, other_gender_row], ignore_index=True)

        cleaned_data = self.cleaning_instance.remove_rows_with_other_gender()
        self.assertFalse(any(cleaned_data["gender"] == "Other"))


class MockIsolationForest:
    """
    Helper class for mocking IsolationForest
    """
    def fit_predict(self, X):
        """
        Mock method to return -1 for each sample in X
        """
        return [-1] * len(X)


if __name__ == "__main__":
    unittest.main()
