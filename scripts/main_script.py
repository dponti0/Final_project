
# The main script will call the plotting script (branch!) + predective modeling

# main_script.py
import pandas as pd
import matplotlib.backends.backend_pdf as pdf_backend
from univariate_analysis import UnivariateVisualizer
import os

def main():
    
    data = pd.read_csv("outputs/cleaned_dataset.csv")

    # Crear la carpeta 'outputs' si no existe
    os.makedirs("outputs", exist_ok=True)

    # Crear un objeto PdfPages para almacenar los gráficos en un solo PDF
    pdf_path = "outputs/univariate_analysis.pdf"
    pdf_pages = pdf_backend.PdfPages(pdf_path)

    # Crear una instancia de la clase UnivariateVisualizer
    visualizer = UnivariateVisualizer(data, pdf_pages)

    # Llamar a los métodos de visualización (univariate)
    visualizer.visualize_age_distribution()
    visualizer.visualize_age_group_distribution()
    visualizer.visualize_gender_distribution()
    visualizer.visualize_hypertension_distribution()
    visualizer.visualize_heart_disease_distribution()
    visualizer.visualize_strokes_distribution()
    visualizer.visualize_glucose_distribution()
    visualizer.visualize_bmi_distribution()
    visualizer.visualize_smoking_distribution()
    visualizer.visualize_work_type_distribution()
    visualizer.visualize_marital_status_distribution()
    visualizer.visualize_residence_type_distribution()

    # Cerrar el objeto PdfPages para finalizar el PDF
    pdf_pages.close()

    print()
    print(f"The PDF report including the univariate analysis has been saved at: {pdf_path}")

if __name__ == "__main__":
    print("The main script is properly running!!")
    main()

# python scripts/main_script.py
    