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
        plt.title("Age Distribution", weight='bold')
        plt.xlabel("Age", fontstyle='italic')
        plt.ylabel("Frequency", fontstyle='italic')
        sns.despine()
        self.save_and_close()

    def visualize_age_group_distribution(self):
        # Crea el gráfico
        plt.figure(figsize=(10, 6))
        ax = sns.histplot(x="age_group", data=self.df, bins=20, kde=True, color="skyblue")

        # Ajusta el título superior en negrita
        plt.title("Age Group Distribution", weight='bold')

        # Ajusta los títulos laterales en cursiva
        ax.set_xlabel("Age Group", fontstyle='italic')
        ax.set_ylabel("Frequency", fontstyle='italic')

        # Elimina el marco del gráfico
        sns.despine()

        self.save_and_close()

    def visualize_gender_distribution(self):
        f_df = self.df[self.df['gender'].isin(['male', 'female'])]
        total_samples = len(f_df)
        gender_percentages = f_df['gender'].value_counts(normalize=True) * 100

        # Configure the style
        sns.set(style="whitegrid")
        plt.figure(figsize=(7, 5))

        # Create the bar plot
        ax = sns.barplot(x=gender_percentages.values, y=gender_percentages.index, palette="pastel")

        # Add percentages on the vertical axis
        for i, percentage in enumerate(gender_percentages):
            ax.text(percentage + 1, i, f'{percentage:.0f}%', va='center', fontweight='bold')

        # Adjust title and labels
        plt.title("Gender Distribution", weight='bold')
        plt.ylabel("Gender", fontstyle='italic', fontsize=9)
        plt.xticks([])

        sns.despine(bottom=True)
        self.save_and_close()

    def visualize_hypertension_distribution(self):
        # Crea el gráfico de pastel
        plt.figure(figsize=(8, 8))
        hypertension_counts = self.df['hypertension'].value_counts()
        colors = sns.color_palette("pastel")

        # Utiliza solo una variable para obtener las características del pie chart
        wedges, _ = plt.pie(hypertension_counts, startangle=90,
                            colors=colors, wedgeprops=dict(width=0.5), shadow=True)

        # Elimina el marco del gráfico
        plt.gca().set_aspect('equal')

        # Ajusta el título para que sea en negrita
        plt.title("Hypertension Distribution", weight='bold')

        # Añade la leyenda con labels personalizados
        plt.legend(labels=["No", "Yes"], loc="upper right", bbox_to_anchor=(1, 0.8), title="Hypertension")

        self.save_and_close()


    def visualize_heart_disease_distribution(self):
        # Crea el gráfico de pastel
        plt.figure(figsize=(8, 8))
        heart_disease_counts = self.df['heart_disease'].value_counts()
        colors = sns.color_palette("pastel")

        # Utiliza solo una variable para obtener las características del pie chart
        _ = plt.pie(heart_disease_counts, startangle=90,
                    colors=colors, wedgeprops=dict(width=0.5), labeldistance=1.2, shadow=True)

        # Elimina el marco del gráfico
        plt.gca().set_aspect('equal')

        # Ajusta el título para que sea en negrita
        plt.title("Heart Disease Distribution", weight='bold')

        # Añade la leyenda con labels personalizados
        plt.legend(labels=["No", "Yes"], loc="upper right", bbox_to_anchor=(1, 0.8), title="Heart Disease")

        self.save_and_close()

    def visualize_glucose_distribution(self):
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df["avg_glucose_level"], bins=20, kde=True, color="orange")
        plt.title("Glucose Levels Distribution", weight='bold')
        plt.xlabel("Glucose Level", fontstyle='italic')
        plt.ylabel("Frequency", fontstyle='italic')
        sns.despine()
        self.save_and_close()

    def visualize_bmi_distribution(self):
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df["bmi"].dropna(), bins=20, kde=True, color="green")
        plt.title("Body Mass Index (BMI) Distribution", weight='bold')
        plt.xlabel("BMI", fontstyle='italic')
        plt.ylabel("Frequency", fontstyle='italic')
        sns.despine()
        self.save_and_close()



    def visualize_work_type_distribution(self):
        # Establece el estilo de seaborn
        sns.set_style("whitegrid")

        # Configura la paleta de colores
        palette = sns.color_palette("Blues_d")

        # Crea el gráfico
        plt.figure(figsize=(10, 6))
        ax = sns.countplot(x="work_type", data=self.df, palette=palette, edgecolor="none")

        # Añade líneas horizontales grises
        ax.yaxis.grid(True, linestyle='--', alpha=0.7, color='gray')

        # Ajusta el título superior en negrita
        plt.title("Work Type Distribution", weight='bold')

        # Ajusta los títulos laterales en cursiva
        ax.set_xlabel("Work Type", fontstyle='italic', fontsize=10)
        ax.set_ylabel("Number of People", fontstyle='italic', fontsize=10)

        # Elimina el marco del gráfico
        sns.despine()

        self.save_and_close()



    def visualize_marital_status_distribution(self):
        plt.figure(figsize=(7, 7))
        marital_status_counts = self.df['ever_married'].value_counts()
        colors = sns.color_palette("pastel")

        _ = plt.pie(marital_status_counts, startangle=90, colors=colors, wedgeprops=dict(width=0.5), shadow=True)

        # Elimina el marco del gráfico
        plt.gca().set_aspect('equal')
        
        # Ajusta el título para que sea en negrita
        plt.title("Marital Status Distribution", weight='bold')

        # Agrega un label
        plt.legend(labels=marital_status_counts.index, loc="upper right", bbox_to_anchor=(1, 0.8), title="Marital Status")

        self.save_and_close()

    def visualize_residence_type_distribution(self):
        plt.figure(figsize=(7, 7))
        residence_type_counts = self.df['Residence_type'].value_counts()
        colors = sns.color_palette("pastel")

        wedges, _ = plt.pie(residence_type_counts, startangle=90, colors=colors, wedgeprops=dict(width=0.4), 
                            textprops=dict(weight='bold'), labeldistance=1.2, shadow=True)  # Añade shadow=True para sombras

        # Elimina el marco del gráfico
        plt.gca().set_aspect('equal')
        
        # Ajusta el título para que sea en negrita
        plt.title("Residence Type Distribution", weight='bold')

        # Agrega un label
        plt.legend(labels=residence_type_counts.index, loc="upper right", bbox_to_anchor=(1, 0.8), title="Residence Type")

        self.save_and_close()


    def visualize_smoking_distribution(self):
        # Establece el estilo de seaborn
        sns.set_style("whitegrid")

        # Configura la paleta de colores
        palette = sns.color_palette("Blues_d")

        # Crea el gráfico
        plt.figure(figsize=(8, 5))
        ax = sns.countplot(x="smoking_status", data=self.df, palette=palette, edgecolor="none")

        # Añade líneas horizontales grises
        ax.yaxis.grid(True, linestyle='--', alpha=0.7, color='gray')

        # Ajusta el título superior en negrita
        plt.title("Smoking Distribution", weight='bold')

        # Ajusta los títulos laterales en cursiva
        ax.set_xlabel("Smoking Status", fontstyle='italic')
        ax.set_ylabel("Number of People", fontstyle='italic')

        # Elimina el marco del gráfico
        sns.despine()

        self.save_and_close()


    def visualize_strokes_distribution(self):
        # Crea el gráfico de pastel
        plt.figure(figsize=(8, 8))
        strokes_counts = self.df['stroke'].value_counts()
        colors = sns.color_palette("pastel")

        # Utiliza solo una variable para obtener las características del pie chart
        _ = plt.pie(strokes_counts, startangle=90,
                    colors=colors, wedgeprops=dict(width=0.4), labeldistance=1.2, shadow=True)
        
        # Elimina el marco del gráfico
        plt.gca().set_aspect('equal')
        
        # Ajusta el título para que sea en negrita
        plt.title("Stroke Distribution", weight='bold')

        plt.legend(labels=["Yes", "No"], loc="upper right", bbox_to_anchor=(1, 0.8), title="Stroke")

        self.save_and_close()
