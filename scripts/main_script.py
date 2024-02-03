
# The main script will call the plotting script (branch!) + predective modeling

# main_script.py
import pandas as pd
import matplotlib.backends.backend_pdf as pdf_backend
from univariate_analysis import UnivariateVisualizer
from multivariate_analysis import MultivariateVisualizer
import os

def main():
    
    data = pd.read_csv("outputs/cleaned_dataset.csv")

    # Crear la carpeta 'outputs' si no existe
    os.makedirs("outputs", exist_ok=True)

    # Crear un objeto PdfPages para almacenar los gráficos en un solo PDF
    uni_pdf_path = "outputs/univariate_analysis.pdf"
    bi_pdf_path = "outputs/multivariate_analysis.pdf"

    uni_pdf_pages = pdf_backend.PdfPages(uni_pdf_path)
    bi_pdf_pages = pdf_backend.PdfPages(bi_pdf_path)

    # Crear instancias de la clase UnivariateVisualizer y MultivariateVisualizer
    uni_visualizer = UnivariateVisualizer(data, uni_pdf_pages)
    bi_visualizer = MultivariateVisualizer(data, bi_pdf_pages)

    # Llamar a los métodos de visualización (univariate)

    def visualize_univariate_relationships(uni_visualizer):
        """
        Visualize univariate distributions using the provided UniVisualizer instance
        """  
        uni_visualizer.visualize_age_distribution()
        uni_visualizer.visualize_age_group_distribution()
        uni_visualizer.visualize_gender_distribution()
        uni_visualizer.visualize_hypertension_distribution()
        uni_visualizer.visualize_heart_disease_distribution()
        uni_visualizer.visualize_strokes_distribution()
        uni_visualizer.visualize_glucose_distribution()
        uni_visualizer.visualize_bmi_distribution()
        uni_visualizer.visualize_smoking_distribution()
        uni_visualizer.visualize_work_type_distribution()
        uni_visualizer.visualize_marital_status_distribution()
        uni_visualizer.visualize_residence_type_distribution()

    def visualize_multivariate_relationships(bi_visualizer):
        """
        Visualize multivariate distributions using the provided MultiVisualizer instance
        """
        bi_visualizer.age_stroke_distribution()
        bi_visualizer.glucose_stroke_distribution()
        bi_visualizer.bmi_stroke_distribution()
        bi_visualizer.bmi_glucose_scatter()
        bi_visualizer.heart_disease_gender_age()
        bi_visualizer.glucose_smoking_distribution()
        bi_visualizer.age_bmi_relation()
        bi_visualizer.work_type_stroke_distribution()
        bi_visualizer.marriage_glucose_relation()
        bi_visualizer.marriage_bmi_relation()
        bi_visualizer.age_stroke_rate_lineplot()
        bi_visualizer.correlation_heatmap()

    visualize_univariate_relationships(uni_visualizer)
    visualize_multivariate_relationships(bi_visualizer)

    # Cerrar los objetos PdfPages para finalizar los PDFs
    uni_pdf_pages.close()
    bi_pdf_pages.close()

    print()
    print(f"The PDF report including univariate analysis has been saved at: {uni_pdf_path}")
    print(f"The PDF report including multivariate analysis has been saved at: {bi_pdf_path}")

if __name__ == "__main__":
    print("The main script is properly running!!")
    main()

# python scripts/main_script.py
    