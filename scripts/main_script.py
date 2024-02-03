
# The main script will call the plotting script (branch!) + predective modeling

# main_script.py
import pandas as pd
import matplotlib.backends.backend_pdf as pdf_backend
from univariate_analysis import visualize_age_distribution, visualize_age_group_distribution, visualize_gender_distribution, visualize_hypertension_distribution, visualize_heart_disease_distribution, visualize_strokes_distribution, visualize_glucose_distribution, visualize_bmi_distribution, visualize_smoking_distribution, visualize_work_type_distribution, visualize_marital_status_distribution, visualize_residence_type_distribution
import os

def main():
    
    data = pd.read_csv("outputs/cleaned_dataset.csv")

    # Crear la carpeta 'outputs' si no existe
    os.makedirs("outputs", exist_ok=True)

    # Crear un objeto PdfPages para almacenar los gráficos en un solo PDF
    pdf_path = "outputs/univariate_analysis.pdf"
    pdf_pages = pdf_backend.PdfPages(pdf_path)

    # Llamar a funciones para visualizar y guardar los gráficos en la carpeta 'outputs'
    visualize_age_distribution(data, "outputs/age_distribution_plot.png", pdf_pages)
    visualize_age_group_distribution(data, "outputs/age_group_plot.png", pdf_pages)
    visualize_gender_distribution(data, "outputs/gender_distribution_plot.png", pdf_pages)
    visualize_hypertension_distribution(data, "outputs/hypertension_plot.png", pdf_pages)
    visualize_heart_disease_distribution(data, "outputs/heartdisease_plot.png", pdf_pages)
    visualize_strokes_distribution(data, "outputs/strokes_plot.png", pdf_pages)
    visualize_glucose_distribution(data, "outputs/glucose_distribution_plot.png", pdf_pages)
    visualize_bmi_distribution(data, "outputs/bmi_distribution_plot.png", pdf_pages)
    visualize_smoking_distribution(data, "outputs/smoking_distribution_plot.png", pdf_pages)
    visualize_work_type_distribution(data, "outputs/work_type_distribution_plot.png", pdf_pages)
    visualize_marital_status_distribution(data, "outputs/marital_status_distribution_plot.png", pdf_pages)
    visualize_residence_type_distribution(data, "outputs/residence_type_distribution_plot.png", pdf_pages)

    # Cerrar el objeto PdfPages para finalizar el PDF
    pdf_pages.close()

    print()
    print(f"The PDF report including the univariate analysis has been saved at: {pdf_path}")

if __name__ == "__main__":
    print("The main script is properly running!!")
    main()

# python scripts/main_script.py
    