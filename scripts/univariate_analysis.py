# univariate_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class UnivariateVisualizer:
    def __init__(self, df, pdf_pages=None):
        self.df = df
        self.pdf_pages = pdf_pages

    def save_and_close(self):
        if self.pdf_pages:
            self.pdf_pages.savefig()
        plt.close()

    def visualize_age_distribution(self):
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df["age"], bins=20, kde=True, color="skyblue")
        plt.title("Age Distribution")
        plt.xlabel("Age")
        plt.ylabel("Frequency")
        self.save_and_close()

    def visualize_age_group_distribution(self):
        plt.figure(figsize=(10, 6))
        sns.countplot(x="age_group", data=self.df, palette="muted")
        plt.title("Age Group Distribution")
        plt.xlabel("Age Group")
        plt.ylabel("Number of People")
        self.save_and_close()

    def visualize_gender_distribution(self):
        plt.figure(figsize=(8, 5))
        sns.countplot(x="gender", data=self.df, palette="pastel")
        plt.title("Gender Distribution")
        plt.xlabel("Gender")
        plt.ylabel("Number of People")
        self.save_and_close()

    def visualize_hypertension_distribution(self):
        plt.figure(figsize=(8, 5))
        ax = sns.countplot(x="hypertension", data=self.df, palette="Set2")
        plt.title("Hypertension Distribution")
        plt.xlabel("Hypertension")
        plt.ylabel("Number of People")
        ax.set_xticklabels(["No", "Yes"])

        # Agrega el recuento en la leyenda
        counts = self.df["hypertension"].value_counts()
        for i, count in enumerate(counts):
            ax.text(i, count + 1, str(count), ha='center')

        self.save_and_close()

    def visualize_heart_disease_distribution(self):
        plt.figure(figsize=(8, 5))
        ax = sns.countplot(x="heart_disease", data=self.df, palette="Set2")
        plt.title("Heart Disease Distribution")
        plt.xlabel("Heart Disease")
        plt.ylabel("Number of People")
        ax.set_xticklabels(["No", "Yes"])

        # Agrega el recuento en la leyenda
        counts = self.df["heart_disease"].value_counts()
        for i, count in enumerate(counts):
            ax.text(i, count + 1, str(count), ha='center')

        self.save_and_close()

    def visualize_strokes_distribution(self):
        plt.figure(figsize=(8, 5))
        ax = sns.countplot(x="stroke", data=self.df, palette="Set2")
        plt.title("Stroke Distribution")
        plt.xlabel("Stroke")
        plt.ylabel("Number of People")
        ax.set_xticklabels(["No", "Yes"])

        # Agrega el recuento en la leyenda
        counts = self.df["stroke"].value_counts()
        for i, count in enumerate(counts):
            ax.text(i, count + 1, str(count), ha='center')

        self.save_and_close()

    def visualize_glucose_distribution(self):
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df["avg_glucose_level"], bins=20, kde=True, color="orange")
        plt.title("Glucose Levels Distribution")
        plt.xlabel("Glucose Level")
        plt.ylabel("Frequency")
        self.save_and_close()

    def visualize_bmi_distribution(self):
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df["bmi"].dropna(), bins=20, kde=True, color="green")
        plt.title("Body Mass Index (BMI) Distribution")
        plt.xlabel("BMI")
        plt.ylabel("Frequency")
        self.save_and_close()

    def visualize_smoking_distribution(self):
        plt.figure(figsize=(8, 5))
        sns.countplot(x="smoking_status", data=self.df, palette="pastel")
        plt.title("Smoking Distribution")
        plt.xlabel("Smoking Status")
        plt.ylabel("Number of People")
        self.save_and_close()

    def visualize_work_type_distribution(self):
        plt.figure(figsize=(10, 6))
        sns.countplot(x="work_type", data=self.df, palette="viridis")
        plt.title("Work Type Distribution")
        plt.xlabel("Work Type")
        plt.ylabel("Number of People")
        self.save_and_close()

    def visualize_marital_status_distribution(self):
        plt.figure(figsize=(8, 5))
        sns.countplot(x="ever_married", data=self.df, palette="pastel")
        plt.title("Marital Status Distribution")
        plt.xlabel("Marital Status")
        plt.ylabel("Number of People")
        self.save_and_close()

    def visualize_residence_type_distribution(self):
        plt.figure(figsize=(8, 5))
        sns.countplot(x="Residence_type", data=self.df, palette="pastel")
        plt.title("Residence Type Distribution")
        plt.xlabel("Residence Type")
        plt.ylabel("Number of People")
        self.save_and_close()
