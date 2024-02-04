"""
Script for feature engineering study using the clean dataset
"""

# Import the required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Input, output and loading the dataset
input_path = 'outputs/cleaned_dataset.csv'
output_path = 'outputs/cleaned_dataset.csv'  # Overwrite the same file
df = pd.read_csv(input_path)

def determine_overall_health(row):
    """
    Function to establish the conditions of the new column
    """
    if row['stroke'] == 1:
        return 'Very Bad'
    elif row['hypertension'] == 1 or row['heart_disease'] == 1 or row['bmi'] >= 30:
        return 'Bad'
    elif row['ever_married'] == 'yes' and row['work_type'] == 'private' and row['smoking_status'] == 'smokes':
        return 'Regular'
    elif row['age'] >= 60 and row['avg_glucose_level'] >= 140:
        return 'Bad'
    elif row['age'] >= 50 and row['bmi'] >= 25:
        return 'Regular'
    elif row['gender'] == 'female' and row['age'] >= 40 and row['age'] <= 60 and row['heart_disease'] == 0:
        return 'Good'
    elif row['gender'] == 'male' and row['age'] >= 40 and row['age'] <= 60 and row['hypertension'] == 0:
        return 'Good'
    elif row['work_type'] == 'self-employed' and row['smoking_status'] == 'never smoked':
        return 'Good'
    elif 40 <= row['age'] <= 60:
        if row['gender'] == 'female' and row['heart_disease'] == 0 and row['smoking_status'] == 'never smoked':
            return 'Very Good'
        elif row['gender'] == 'male' and row['hypertension'] == 0 and row['smoking_status'] == 'never smoked':
            return 'Very Good'
        elif row['gender'] == 'female' and row['heart_disease'] == 0 and row['smoking_status'] == 'formerly smoked':
            return 'Good'
        elif row['gender'] == 'male' and row['hypertension'] == 0 and row['smoking_status'] == 'formerly smoked':
            return 'Good'
    elif row['age'] < 18 and (row['avg_glucose_level'] >= 110 or row['bmi'] >= 25):
        return 'Bad'
    elif row['age'] >= 18 and row['age'] < 30 and row['bmi'] >= 25:
        return 'Regular'
    elif row['age'] >= 30 and row['age'] < 50 and row['bmi'] >= 28:
        return 'Regular'
    elif row['age'] >= 50 and row['bmi'] >= 28:
        return 'Regular'
    else:
        return 'Very Good'

def create_overall_health_column(df):
    """
    Function to create a new column based on the previous function
    """
    df['overall_health'] = df.apply(determine_overall_health, axis=1)
    return df

if __name__ == '__main__':
    print("The feature engineering script is properly running!!")
    print()
    
    try:
        # Create the 'overall_health' column
        df = create_overall_health_column(df)

        # Save the dataset with the new column
        df.to_csv(output_path, index=False)

        # Ilustrate that the new column has been added and changes saved
        print("The 'overall_health' column has been added to the cleaned dataset.")
        print("Changes have been saved to:", output_path)


    except Exception as e:
        # Handle exceptions and print an error message
        print(f"An error occurred: {e}")

# Close the file
plt.close()