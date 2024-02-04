# regression_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

def train_regression_model(X, y):
    # Identify numerical and categorical columns
    numerical_cols = X.select_dtypes(include=['float64']).columns
    categorical_cols = X.select_dtypes(include=['object']).columns

    # Create transformers for numerical and categorical columns
    numerical_transformer = Pipeline(steps=[('scaler', StandardScaler())])
    categorical_transformer = Pipeline(steps=[('onehot', OneHotEncoder())])

    # Combine transformers using ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ])

    # Combine preprocessing with model in a pipeline
    model = Pipeline([
        ('preprocessor', preprocessor),
        ('regression', RandomForestRegressor(n_estimators=100, random_state=42))  # You can adjust parameters
    ])

    # Train the model
    model.fit(X, y)
    return model

def evaluate_model(model, X_test, y_test):
    # Predict on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model performance
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    rounded_mse = round(mse, 4)  # Round the MSE to 4 decimal places
    rounded_r2 = round(r2, 4)  # Round the R-squared to 4 decimal places

    print(f'Mean Squared Error on Test Set: {rounded_mse}')
    print(f'R-squared on Test Set: {rounded_r2}')

    # Save the results to a text file
    with open('outputs/stroke_prediction.txt', 'w') as file:
        file.write(f'Mean Squared Error on Test Set: {rounded_mse}\n')
        file.write(f'R-squared on Test Set: {rounded_r2}\n')

    # Closing    
    print("\nClosing comments:")
    print("The trained model can now be used to predict the risk of stroke based on input features.")
    print("The Mean Squared Error (MSE) and R-squared values provide insights into the model's accuracy and goodness of fit.")
    print("Further analysis and interpretation of feature importance can help understand the factors influencing stroke risk predictions.")
    print("Users can utilize the saved model (`regression_model.joblib`) for making predictions on new data.\n")

if __name__ == '__main__':
    # Specify input and output paths
    input_path = 'outputs/cleaned_dataset.csv'
    output_path = 'outputs/data_with_stroke_risk.csv'

    # Load the dataset
    df = pd.read_csv(input_path)

    # Separate features (X) and the target variable (y)
    X = df.drop(['id', 'stroke'], axis=1)
    y = df['stroke']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the regression model
    regression_model = train_regression_model(X_train, y_train)

    # Evaluate and print model performance
    evaluate_model(regression_model, X_test, y_test)

    # Save the trained model in the current working directory
    joblib.dump(regression_model, 'regression_model.joblib')
