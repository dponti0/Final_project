
# The main script will call the plotting script (branch!) + predective modeling

# main_script.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from filtering import FilteringClass
import os

def main():
    # Cargar datos desde la carpeta 'outputs'
    data = pd.read_csv("outputs/cleaned_dataset.csv")

    # Crear la carpeta 'outputs' si no existe (corroborar que existe)
    os.makedirs("outputs", exist_ok=True)

    # Inicializar la clase de filtrado
    filter_instance = FilteringClass(data)

    # Filtrar por hipertensión, enfermedad cardíaca, alto nivel de glucosa, alto BMI y accidente cerebrovascular
    hypertension_data = filter_instance.filter_by_hypertension()
    heartdis_data = filter_instance.filter_by_heart_disease()
    glucose_data = filter_instance.filter_by_high_glucose()
    bmi_data = filter_instance.filter_by_high_bmi()
    strokes_data = filter_instance.filter_by_stroke()

    # Visualizar y guardar resultados para cada filtro
    visualize_and_save(hypertension_data, "Hypertension", "outputs/hypertension_plot.png")
    visualize_and_save(heartdis_data, "Heart Disease", "outputs/heart_disease_plot.png")
    visualize_and_save(glucose_data, "High Glucose", "outputs/high_glucose_plot.png")
    visualize_and_save(bmi_data, "High BMI", "outputs/high_bmi_plot.png")
    visualize_and_save(strokes_data, "Stroke", "outputs/stroke_plot.png")

def visualize_and_save(data, title, save_path):
    # Código para visualizar resultados
    plt.figure(figsize=(10, 6))
    sns.countplot(x='alguna_columna', data=data)  # Ajusta la columna según tu conjunto de datos
    plt.title(f"{title} Visualization")
    plt.xlabel("X Label")
    plt.ylabel("Y Label")
    plt.savefig(save_path)  # Guardar el gráfico en la carpeta 'outputs'
    plt.show()

if __name__ == "__main__":
    print("The main script is properly running!!")
    main()
