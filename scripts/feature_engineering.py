# feature_engineering_script.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib

def feature_engineering(input_data_path, output_data_path, model_path):
    # Cargar el conjunto de datos
    df = pd.read_csv(input_data_path)

    # Separar las features (X) y la variable objetivo (y)
    X = df.drop(['id', 'Life Expectancy'], axis=1)
    y = df['Life Expectancy']

    # Dividir el conjunto de datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crear un modelo de regresión lineal
    model = Pipeline([
        ('scaler', StandardScaler()),
        ('regression', LinearRegression())
    ])

    # Entrenar el modelo
    model.fit(X_train, y_train)

    # Predecir en el conjunto de prueba
    y_pred = model.predict(X_test)

    # Evaluar el rendimiento del modelo
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error on Test Set: {mse}')

    # Guardar el modelo entrenado
    joblib.dump(model, model_path)

    # Crear una nueva columna 'Life Expectancy' en el conjunto de datos original
    df['Life Expectancy'] = model.predict(X)

    # Guardar el conjunto de datos con la nueva columna
    df.to_csv(output_data_path, index=False)

if __name__ == '__main__':
    # Especificar rutas de entrada y salida
    input_data_path = 'path/to/your/input/data.csv'
    output_data_path = 'path/to/your/output/data_with_life_expectancy.csv'
    model_path = 'path/to/your/model/model.joblib'

    # Ejecutar el script de feature engineering
    feature_engineering(input_data_path, output_data_path, model_path)
