import unittest
import pandas as pd
from sklearn.ensemble import IsolationForest
from unittest.mock import patch

def remove_outliers(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Remove outliers from a DataFrame using Isolation Forest."""
    df = df.dropna(subset=columns)
    clf = IsolationForest(contamination=0.05)
    outliers_mask = clf.fit_predict(df[columns]) == -1
    df = df[~outliers_mask]
    return df

class TestOutlierRemoval(unittest.TestCase):
    """Test case for the remove_outliers function."""
    @patch('pandas.read_csv')
    @patch('sklearn.ensemble.IsolationForest')
    def test_remove_outliers(self, mock_isolation_forest, mock_read_csv):
        """Mocks IsolationForest and DataFrame loaded from CSV, then asserts the behavior of removing outliers from the DataFrame."""
        mock_isolation_forest.return_value.fit_predict.return_value = [1] * 8 + [-1, -1]  # Mocking two outliers in the last two rows
        mock_read_csv.return_value = pd.DataFrame({'feature1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'feature2': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]})
        columns_to_remove_outliers = ['feature1', 'feature2']
        result_df = remove_outliers(pd.read_csv('dummy_path.csv'), columns_to_remove_outliers)
        self.assertIsInstance(result_df, pd.DataFrame)
        self.assertEqual(len(result_df), 9)  # Expecting one outlier to be removed

if __name__ == '__main__':
    unittest.main()
