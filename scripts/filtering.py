"""
Script to filter the dataframe by desease
"""

import pandas as pd

class FilteringClass:
    """
    Class for filtering operations  
    """

    def __init__(self, df: pd.DataFrame):
        """
        Initialize the class with a DataFrame
        """
        self.df = df

    def filter_by_hypertension(self) -> pd.DataFrame:
        """
        Filter the DataFrame to keep only individuals with hypertension
        """
        return self.df[self.df['hypertension'] == 1]

    def filter_by_heart_disease(self) -> pd.DataFrame:
        """
        Filter the DataFrame to keep only individuals with heart disease
        """
        return self.df[self.df['heart_disease'] == 1]

    def filter_by_high_glucose(self, glucose_threshold: float) -> pd.DataFrame:
        """
        Filter the DataFrame to keep only individuals with high glucose levels
        """
        glucose_threshold = 125
        return self.df[self.df['avg_glucose_level'] > glucose_threshold]

    def filter_by_high_bmi(self, bmi_threshold: float) -> pd.DataFrame:
        """
        Filter the DataFrame to keep only individuals with high BMI
        """
        bmi_threshold = 30    # Obesity
        return self.df[self.df['bmi'] > bmi_threshold]

    def filter_by_stroke(self) -> pd.DataFrame:
        """
        Filter the DataFrame to keep only individuals who had a stroke
        """
        return self.df[self.df['stroke'] == 1]
