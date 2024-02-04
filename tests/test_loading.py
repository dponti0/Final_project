import pandas as pd
import pytest
from scripts.data_cleaning import load_dataset

@pytest.mark.parametrize("filename, expected_result", [
    ("correct_extension.csv", True),  # Correct extension, expect success
    ("incorrect_extension.txt", False),  # Incorrect extension, expect failure
    ("another_correct_extension.csv", True),  # Correct extension, expect success
])
def test_load_dataset(filename, expected_result):
    try:
        df = load_dataset(filename)
        assert isinstance(df, pd.DataFrame) == expected_result
    except TypeError as e:
        assert "The extension is" in str(e) and expected_result is False

# Use xfail to mark the test case where failure is expected due to incorrect extension
@pytest.mark.xfail(raises=TypeError)
def test_load_dataset_incorrect_extension():
    load_dataset("incorrect_extension.txt")