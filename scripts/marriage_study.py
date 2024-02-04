"""
Script that performs a hypothesis test (chi2) to analyze the association between marital status 
and heart diseases
"""

# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
from matplotlib.backends.backend_pdf import PdfPages
import os

def perform_hypothesis_testing(dataset_path, output_path, save_plot=True):
    """
    Function to perform the chi2 test and conduct the study
    """
    
    print("\nThe marriage study is working correctly!!\n")

    df = pd.read_csv(dataset_path)

    # Relevant columns
    columns_of_interest = ["ever_married", "heart_disease", "hypertension", "stroke"]
    selected_data = df[columns_of_interest]

    # Contingency table
    contingency_table = pd.crosstab(selected_data["ever_married"], selected_data["heart_disease"])

    # Chi-square test
    chi2, p, _, _ = chi2_contingency(contingency_table)

    # Round the numbers
    chi2_rounded = round(chi2, 2)
    p_rounded = round(p, 3)

    # Interpret results
    alpha = 0.05
    hypothesis_result = "Reject" if p < alpha else "Fail to reject"

    # Check and create the output path directory if it doesn't exist
    output_folder = os.path.dirname(output_path)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save the plot and the comments in the same PDF file
    with PdfPages(output_path) as pdf:

        plt.figure(figsize=(10, 6))

        # Shades of blue for the bars
        colors = sns.color_palette("Blues", n_colors=len(contingency_table.columns))

        # Access columns using the unique values as labels
        sns.barplot(x=contingency_table.index, y=contingency_table[contingency_table.columns[1]], label="With disease", color=colors[0], edgecolor='black')
        sns.barplot(x=contingency_table.index, y=contingency_table[contingency_table.columns[0]], bottom=contingency_table[contingency_table.columns[1]], label="Without disease", color=colors[-1], edgecolor='black')

        # Labels and legend
        plt.title("Relationship between Marital Status and Heart Diseases", fontweight='bold')
        plt.xlabel("Marital Status", fontstyle="italic")
        plt.ylabel("Number of People", fontstyle="italic")
        plt.legend(title="Disease")

        # Remove the border lines
        sns.despine()

        # Hypothesis, conclusion and interpretation message
        hypothesis_text = f"Hypothesis: The presence of heart diseases is associated with marital status."
        conclusion_text = f"Conclusion: {hypothesis_result} the null hypothesis with a significance level of {alpha}."

        interpretation_text = (
            "Interpretation: Rejecting the null hypothesis indicates that there is sufficient evidence "
            "to suggest an association between marital status and heart disease in the given population."
        )

        # Add text to the plot & close
        plt.text(0.5, -0.15, hypothesis_text, color='black', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
        plt.text(0.5, -0.25, f"Chi2 Value: {chi2_rounded}", color='black', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
        plt.text(0.5, -0.3, f"P-value: {p_rounded}", color='black', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
        plt.text(0.5, -0.2, conclusion_text, color='black', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
        plt.text(0.5, -0.35, interpretation_text, color='black', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)

        pdf.savefig(bbox_inches="tight")
        plt.close()

    # Display the result
    print("Result obtained in the study:")
    print("Chi2_value:", chi2_rounded)
    print("P_value:", p_rounded)
    print("Hypothesis result:", hypothesis_result)
    
    # Print the interpretation & the output path
    print("\n" + "=" * 50)
    print(interpretation_text[16:])
    print("=" * 50)
    print()

    print(f"\nThe file was correctly saved as: {output_path}\n")

dataset_path = "outputs/cleaned_dataset.csv"
output_path = "outputs/marriage_study.pdf"
perform_hypothesis_testing(dataset_path, output_path, save_plot=True)

