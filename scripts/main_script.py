"""
The main script, used for elaborating the entire study by mainly calling other functions
and grouping them all in one same script
"""

# Import the required libraries
import os
import subprocess
import pandas as pd
import matplotlib.backends.backend_pdf as pdf_backend
from univariate_analysis import UnivariateVisualizer
from multivariate_analysis import MultivariateVisualizer
import pdb

# Define paths
CLEANED_DATASET_PATH = "outputs/cleaned_dataset.csv"
UNIVARIATE_PDF_PATH = "outputs/univariate_analysis.pdf"
MULTIVARIATE_PDF_PATH = "outputs/multivariate_analysis.pdf"
FEATURE_ENGINEERING_SCRIPT_PATH = "scripts/feature_engineering.py"
REGRESSION_MODEL_PATH = "scripts/regression_model.py"
MARRIAGE_STUDY_PATH = "outputs/marriage_study.pdf"


# Define the functions for runing each script
def run_feature_engineering_script():
    """
    Function for running the feature engineering script
    """
    try:
        subprocess.run(["python", FEATURE_ENGINEERING_SCRIPT_PATH])
    except Exception as e:
        print(f"Error while running the feature engineering script: {e}")


def run_regression_model_script():
    """
    Function for running the predictive modeling script
    """
    try:
        subprocess.run(["python", REGRESSION_MODEL_PATH])
    except Exception as e:
        print(f"Error while running the regression model script: {e}")


def run_marriage_study_script():
    """
    Function for running the marriage study
    """
    try:
        subprocess.run(["python", MARRIAGE_STUDY_PATH])
    except Exception as e:
        print(f"Error while running the hypothesis testing script: {e}")


def visualize_univariate_relationships(uni_visualizer):
    """
    Visualize univariate distributions using the provided UniVisualizer instance
    """
    uni_visualizer.visualize_gender_distribution()
    uni_visualizer.visualize_age_distribution()
    uni_visualizer.visualize_age_group_distribution()
    uni_visualizer.visualize_hypertension_distribution()
    uni_visualizer.visualize_heart_disease_distribution()
    uni_visualizer.visualize_glucose_distribution()
    uni_visualizer.visualize_strokes_distribution()
    uni_visualizer.visualize_bmi_distribution()
    uni_visualizer.visualize_smoking_distribution()
    uni_visualizer.visualize_marital_status_distribution()
    uni_visualizer.visualize_work_type_distribution()
    uni_visualizer.visualize_residence_type_distribution()


def visualize_multivariate_relationships(bi_visualizer):
    """
    Visualize multivariate distributions using the provided MultiVisualizer instance
    """
    bi_visualizer.age_stroke_rate_lineplot()
    bi_visualizer.age_stroke_distribution()
    bi_visualizer.overall_health_pie_chart()
    bi_visualizer.bmi_stroke_distribution()
    bi_visualizer.glucose_stroke_distribution()
    bi_visualizer.bmi_glucose_scatter()
    bi_visualizer.heart_disease_gender_age()
    bi_visualizer.glucose_smoking_distribution()
    bi_visualizer.age_bmi_relation()
    bi_visualizer.work_type_stroke_distribution()
    bi_visualizer.marriage_glucose_relation()
    bi_visualizer.marriage_bmi_relation()
    bi_visualizer.correlation_heatmap()


def main():
    """
    Main function
    """

    print("\nThe main script is properly running!!")
    print()

    # Read the cleaned dataset
    data = pd.read_csv(CLEANED_DATASET_PATH)

    # Create the 'outputs' folder if it does not exist
    os.makedirs("outputs", exist_ok=True)

    # Run feature engineering script
    run_feature_engineering_script()

    # Run feature engineering script
    run_regression_model_script()

    # Run feature engineering script
    run_marriage_study_script()

    # Add a breakpoint for debugging
    pdb.set_trace()

    # Create PdfPages objects to store the plots in a single PDF
    uni_pdf_path = "outputs/univariate_analysis.pdf"
    bi_pdf_path = "outputs/multivariate_analysis.pdf"

    uni_pdf_pages = pdf_backend.PdfPages(uni_pdf_path)
    bi_pdf_pages = pdf_backend.PdfPages(bi_pdf_path)

    # Create instances of the UnivariateVisualizer and MultivariateVisualizer classes
    uni_visualizer = UnivariateVisualizer(data, uni_pdf_pages)
    bi_visualizer = MultivariateVisualizer(data, bi_pdf_pages)

    # Call the visualization methods
    visualize_univariate_relationships(uni_visualizer)
    visualize_multivariate_relationships(bi_visualizer)

    # Close PdfPages objects to finalize the PDFs
    uni_pdf_pages.close()
    bi_pdf_pages.close()

    print()
    print(
        f"The PDF report including univariate analysis has been saved at: {uni_pdf_path}"
    )
    print(
        f"The PDF report including multivariate analysis has been saved at: {bi_pdf_path}"
    )


if __name__ == "__main__":
    main()
