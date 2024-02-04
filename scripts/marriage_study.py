import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
from matplotlib.backends.backend_pdf import PdfPages
import os

def perform_hypothesis_testing(dataset_path, output_path, save_plot=True):
    # Load dataset
    df = pd.read_csv(dataset_path)

    # Select relevant columns
    columns_of_interest = ["ever_married", "heart_disease", "hypertension", "stroke"]
    selected_data = df[columns_of_interest]

    # Create a contingency table
    contingency_table = pd.crosstab(selected_data["ever_married"], selected_data["heart_disease"])

    # Perform chi-square test
    chi2, p, _, _ = chi2_contingency(contingency_table)

    # Round the numbers to two decimals
    chi2_rounded = round(chi2, 2)
    p_rounded = round(p, 3)

    # Interpret results
    alpha = 0.05
    hypothesis_result = "Reject" if p < alpha else "Fail to reject"

    # Check and create the output path directory if it doesn't exist
    output_folder = os.path.dirname(output_path)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save both the plot and the comments in the same PDF file
    with PdfPages(output_path) as pdf:
        # Visualize the contingency table as a bar plot with adjusted styling
        plt.figure(figsize=(10, 6))

        # Use shades of blue for the bars
        colors = sns.color_palette("Blues", n_colors=len(contingency_table.columns))

        # Access columns using the unique values as labels
        sns.barplot(x=contingency_table.index, y=contingency_table[contingency_table.columns[1]], label="Con enfermedad", color=colors[0], edgecolor='black')
        sns.barplot(x=contingency_table.index, y=contingency_table[contingency_table.columns[0]], bottom=contingency_table[contingency_table.columns[1]], label="Sin enfermedad", color=colors[-1], edgecolor='black')

        # Add labels and legend
        plt.title("Relación entre Estado Civil y Enfermedades Cardíacas", fontweight='bold')
        plt.xlabel("Estado Civil", fontstyle="italic")
        plt.ylabel("Número de Personas", fontstyle="italic")
        plt.legend(title="Enfermedad")

        # Remove the border lines
        sns.despine()

        # Print the hypothesis, results, and conclusion
        hypothesis_text = f"Hypothesis: La presencia de enfermedades cardíacas está asociada con el estado civil."
        conclusion_text = f"Conclusion: {hypothesis_result} la hipótesis nula con un nivel de significancia de {alpha}."

        # Interpretation of rejecting the hypothesis
        interpretation_text = (
            "Interpretation: Rejecting the null hypothesis indicates that there is sufficient evidence "
            "to suggest an association between marital status and heart disease in the given population."
        )

        # Add text to the plot
        plt.text(0.5, -0.15, hypothesis_text, color='black', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
        plt.text(0.5, -0.2, conclusion_text, color='black', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
        plt.text(0.5, -0.25, f"Chi2 Value: {chi2_rounded}", color='black', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
        plt.text(0.5, -0.3, f"P-value: {p_rounded}", color='black', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
        plt.text(0.5, -0.35, interpretation_text, color='black', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)

        pdf.savefig(bbox_inches="tight")
        plt.close()

    # Display result in different lines
    print("Result obtained in the study:")
    print("Chi2_value:", chi2_rounded)
    print("P_value:", p_rounded)
    print("Hypothesis result:", hypothesis_result)
    
    # Print the simplified interpretation in the terminal
    print("\n" + "=" * 50)
    print(interpretation_text[16:])
    print("=" * 50)
    print()

    print(f"\nThe file was correctly saved as: {output_path}\n")

dataset_path = "outputs/cleaned_dataset.csv"
output_path = "outputs/marriage_study.pdf"
perform_hypothesis_testing(dataset_path, output_path, save_plot=True)

