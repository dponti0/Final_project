import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class BivariateVisualizer:
    def __init__(self, df, pdf_pages=None):
        self.df = df
        self.pdf_pages = pdf_pages

    def save_and_close(self):
        if self.pdf_pages:
            self.pdf_pages.savefig()
        plt.close()
            
    def age_stroke_distribution(self):
        fig, ax = plt.subplots(figsize=(12, 6))

        # Bar plot for age category distribution
        sns.countplot(x='age_cat', hue='stroke', data=self.df, palette='pastel', ax=ax)
        ax.set_title('Age Category-Stroke Distribution', fontweight='bold')  # Título en negrita
        ax.set_xlabel('Age Category', fontstyle='italic')  # Título del eje x en cursiva
        ax.set_ylabel('Count', fontstyle='italic')  # Título del eje y en cursiva

        # Añadir líneas de fondo intermitentes en el eje horizontal
        ax.yaxis.grid(color='gray', linestyle='--', linewidth=0.5)

        # Ajustar leyenda
        ax.legend(title='Stroke', loc='upper right', labels=['No', 'Yes'])

        self.save_and_close()

    def glucose_stroke_distribution(self):
        fig, ax = plt.subplots(figsize=(12, 6))

        # KDE plot for glucose-stroke distribution
        sns.kdeplot(data=self.df, x='avg_glucose_level', hue='stroke', fill=True, common_norm=False, palette='viridis', ax=ax)
        ax.set_title('Distribution of Average Glucose Level by Stroke', fontweight='bold')  # Título en negrita
        ax.set_xlabel('Average Glucose Level', fontstyle='italic')  # Título del eje x en cursiva
        ax.set_ylabel('Density', fontstyle='italic')  # Título del eje y en cursiva

        # Añadir líneas de fondo intermitentes en el eje horizontal
        ax.yaxis.grid(color='gray', linestyle='--', linewidth=0.5)

        # Personalizar la apariencia de los cuadros
        sns.despine(trim=True, left=True, ax=ax)

        self.save_and_close()


    def bmi_stroke_distribution(self):
        fig, ax = plt.subplots(figsize=(12, 6))

        # Violin plot para la distribución BMI-Stroke
        sns.violinplot(x='stroke', y='bmi', data=self.df, palette='Set2', ax=ax)

        # Título y etiquetas de los ejes
        ax.set_title('Distribution of BMI by Stroke', fontweight='bold', fontsize=16)  # Título en negrita y tamaño grande
        ax.set_xlabel('Stroke (0: No, 1: Yes)', fontstyle='italic', fontsize=14)  # Etiqueta del eje x en cursiva y tamaño mediano
        ax.set_ylabel('BMI', fontstyle='italic', fontsize=14)  # Etiqueta del eje y en cursiva y tamaño mediano

        # Decoraciones adicionales
        ax.yaxis.grid(color='gray', linestyle='--', linewidth=0.5)  # Líneas de fondo intermitentes en el eje horizontal

        # Personalizar la apariencia de los cuadros
        sns.despine(trim=True, left=True, ax=ax)

        self.save_and_close()

    def bmi_glucose_scatter(self):
        plt.figure(figsize=(12, 8))
        sns.scatterplot(x='bmi', y='avg_glucose_level', hue='stroke', data=self.df, palette='Set1', alpha=0.7)
        plt.title('BMI-Glucose Scatter Plot with Stroke')
        plt.xlabel('BMI')
        plt.ylabel('Average Glucose Level')
        self.save_and_close()

    def heart_disease_gender_age(self):
        plt.figure(figsize=(12, 6))
        sns.barplot(x='age_group', y='heart_disease', hue='gender', data=self.df, palette='pastel')
        plt.title('Heart Disease per Gender and Age Range')
        plt.xlabel('Age Range')
        plt.ylabel('Heart Disease (0: No, 1: Yes)')
        plt.legend(title='Gender')
        self.save_and_close()


    def glucose_smoking_distribution(self):
        plt.figure(figsize=(12, 6))
        sns.boxplot(x='smoking_status', y='avg_glucose_level', data=self.df, palette='viridis')
        plt.title('Glucose Levels between Smokers and Non-smokers')
        plt.xlabel('Smoking Status')
        plt.ylabel('Average Glucose Level')
        self.save_and_close()


    def age_bmi_relation(self):
        plt.figure(figsize=(12, 6))
        sns.scatterplot(x='age', y='bmi', data=self.df, alpha=0.7)
        plt.title('Age-BMI Relation')
        plt.xlabel('Age')
        plt.ylabel('BMI')
        self.save_and_close()


    def work_type_stroke_distribution(self):
        plt.figure(figsize=(12, 6))
        sns.countplot(x='work_type', hue='stroke', data=self.df, palette='Set1')
        plt.title('Work Type - Stroke Distribution')
        plt.xlabel('Work Type')
        plt.ylabel('Number of People')
        plt.legend(title='Stroke')
        self.save_and_close()


    def marriage_glucose_relation(self):
        plt.figure(figsize=(12, 6))
        sns.boxplot(x='ever_married', y='avg_glucose_level', data=self.df, palette='pastel')
        plt.title('Marriage - Average Glucose Level Relation')
        plt.xlabel('Marital Status (0: No, 1: Yes)')
        plt.ylabel('Average Glucose Level')
        self.save_and_close()


    def marriage_bmi_relation(self):
        plt.figure(figsize=(12, 6))
        sns.boxplot(x='ever_married', y='bmi', data=self.df, palette='Set3')
        plt.title('Marriage - BMI Relation')
        plt.xlabel('Marital Status (0: No, 1: Yes)')
        plt.ylabel('BMI')
        self.save_and_close()
