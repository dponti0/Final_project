"""
Code for filtering
"""
import pandas as pd

class HotelDataFilter:
    """
    Class for filtering operations on a Hotel Reservation DataFrame
    """

    def __init__(self, df: pd.DataFrame):
        """
        Initialize the class with a DataFrame
        """
        self.df = df

    def filter_by_cancellation_status(self, canceled: bool) -> pd.DataFrame:
        """
        Filter the DataFrame based on cancellation status
        """
        return self.df[self.df["is_canceled"] == canceled]

    def filter_by_lead_time(self, max_lead_time: int) -> pd.DataFrame:
        """
        Filter the DataFrame based on lead time
        """
        return self.df[self.df["lead_time"] <= max_lead_time]

    def filter_by_country(self, country: str) -> pd.DataFrame:
        """
        Filter the DataFrame based on the country
        """
        return self.df[self.df["country"] == country]

    def filter_by_stay_length(self, min_weekend_nights: int, min_week_nights: int) -> pd.DataFrame:
        """
        Filter the DataFrame based on the length of stay
        """
        return self.df[
            (self.df["stays_in_weekend_nights"] >= min_weekend_nights)
            & (self.df["stays_in_week_nights"] >= min_week_nights)
        ]

    def filter_by_guests(self, min_adults: int, min_children: int, min_babies: int) -> pd.DataFrame:
        """
        Filter the DataFrame based on the number of guests
        """
        return self.df[
            (self.df["adults"] >= min_adults)
            & (self.df["children"] >= min_children)
            & (self.df["babies"] >= min_babies)
        ]

    def filter_by_meal_option(self, meal_option: str) -> pd.DataFrame:
        """
        Filter the DataFrame based on the meal option
        """
        return self.df[self.df["meal"] == meal_option]
