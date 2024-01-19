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
   
    def filter_by_specific_month(self, month: str) -> pd.DataFrame:
        """
        Filter the DataFrame based on a specific month
        """
        return self.df[self.df["arrival_date_month"] == month]

    def filter_by_week_number(self, week_number: int) -> pd.DataFrame:
        """
        Filter the DataFrame based on a specific week number
        """
        return self.df[self.df["arrival_date_week_number"] == week_number]

    def filter_by_adults_to_children_ratio(self, max_ratio: float) -> pd.DataFrame:
        """
        Filter the DataFrame based on the ratio of adults to children
        """
        return self.df[(self.df["children"] > 0) & (self.df["adults"] / self.df["children"] <= max_ratio)]

    def filter_by_babies(self, min_babies: int) -> pd.DataFrame:
        """
        Filter the DataFrame based on the number of babies
        """
        return self.df[self.df["babies"] >= min_babies]