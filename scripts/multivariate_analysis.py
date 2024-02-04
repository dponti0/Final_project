import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class MultivariateVisualizer:
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

        sns.despine(trim=True, left=True)

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

        ax.legend(labels=['Stroke', 'Non Stroke'], fontsize='8')

        self.save_and_close()


    def bmi_stroke_distribution(self):
        fig, ax = plt.subplots(figsize=(12, 6))

        # Violin plot para la distribución BMI-Stroke
        sns.violinplot(x='stroke', y='bmi', data=self.df, palette='Set2', ax=ax)

        # Título y etiquetas de los ejes
        ax.set_title('Distribution of BMI by Stroke', fontweight='bold', fontsize=14)  # Título en negrita y tamaño grande
        ax.set_xlabel('Stroke (0: No, 1: Yes)', fontstyle='italic', fontsize=10)  # Etiqueta del eje x en cursiva y tamaño mediano
        ax.set_ylabel('BMI', fontstyle='italic', fontsize=10)  # Etiqueta del eje y en cursiva y tamaño mediano

        # Decoraciones adicionales
        ax.yaxis.grid(color='gray', linestyle='--', linewidth=0.5)  # Líneas de fondo intermitentes en el eje horizontal

        # Personalizar la apariencia de los cuadros
        sns.despine(trim=True, left=True, ax=ax)

        self.save_and_close()

    def bmi_glucose_scatter(self):
        plt.figure(figsize=(12, 8))
        
        # Scatter plot for 'No' (stroke=0)
        sns.scatterplot(x='bmi', y='avg_glucose_level', data=self.df[self.df['stroke'] == 0], color='#1f77b4', alpha=0.5, label='No Stroke')
        
        # Scatter plot for 'Yes' (stroke=1)
        sns.scatterplot(x='bmi', y='avg_glucose_level', data=self.df[self.df['stroke'] == 1], color='#ff7f0e', alpha=1, label='Stroke')
        
        plt.title('BMI-Glucose Scatter Plot with Stroke', fontweight='bold')
        plt.xlabel('BMI', fontstyle='italic')
        plt.ylabel('Average Glucose Level', fontstyle='italic')
        plt.legend()
        self.save_and_close()


    def heart_disease_gender_age(self):
        plt.figure(figsize=(12, 6))
        
        sns.barplot(x='age_group', y='heart_disease', hue='gender', data=self.df, palette='pastel')
        
        plt.title('Heart Disease per Gender and Age Range', fontweight='bold')
        plt.xlabel('Age Range', fontstyle='italic')
        plt.ylabel('Heart Disease (0: No, 1: Yes)', fontstyle='italic')
        plt.legend()
        
        self.save_and_close()


    def glucose_smoking_distribution(self):
        plt.figure(figsize=(12, 6))
        
        # Definir colores específicos y etiquetas para las categorías de enfermedades cardíacas
        colors = {0: '#7FB3D5', 1: '#E88E5A'}
        labels = {0: 'Non-Heart Disease', 1: 'Heart Disease'}
        
        # Crear un strip plot en lugar de un swarm plot
        sns.stripplot(x='smoking_status', y='avg_glucose_level', hue='heart_disease', data=self.df,
                    palette=colors, dodge=True, jitter=0.2, size=8)
        
        plt.title('Glucose Levels between Smokers and Non-smokers', fontweight='bold', fontsize=12)
        plt.xlabel('Smoking Status', fontstyle='italic', fontsize=10)
        plt.ylabel('Average Glucose Level', fontstyle='italic', fontsize=10)
        
        # Añadir leyenda con etiquetas y ajustar tamaño
        legend_labels = [plt.Line2D([0], [0], marker='o', color='w', label=labels[i], 
                                markerfacecolor=colors[i], markersize=8) for i in labels]
        
        plt.legend(handles=legend_labels, loc='upper right', bbox_to_anchor=(1, 1), fontsize=6)
        
        # Añadir línea horizontal intermitente con mensaje de threshold de glucosa
        threshold_glucose = 140  
        plt.axhline(y=threshold_glucose, color='gray', linestyle='--', linewidth=0.5)
        plt.text(3, threshold_glucose + 2, 'Threshold Glucose Level', fontstyle='italic', color='black', fontsize=6)
        
        self.save_and_close()

    def age_bmi_relation(self):
        plt.figure(figsize=(12, 6))
        
        # Crear un kdeplot con colores y transparencia
        sns.kdeplot(x='age', y='bmi', data=self.df, fill=True, cmap='coolwarm', levels=5, thresh=0.05)
        
        # Añadir líneas grises intermitentes en el eje horizontal
        plt.axhline(y=20, color='gray', linestyle='--', linewidth=0.8)
        plt.axhline(y=25, color='gray', linestyle='--', linewidth=0.8)
        plt.axhline(y=30, color='gray', linestyle='--', linewidth=0.8)
        
        plt.title('Age-BMI Relation', fontweight='bold', fontsize=12, loc='center')
        plt.xlabel('Age', fontstyle='italic', fontsize=11)
        plt.ylabel('BMI', fontstyle='italic', fontsize=11)
        
        # Añadir etiquetas descriptivas
        plt.text(80, 18, 'Underweight', color='black', fontsize=8, fontstyle='italic')
        plt.text(80, 23, 'Normal Weight', color='black', fontsize=8, fontstyle='italic')
        plt.text(80, 28, 'Overweight', color='black', fontsize=8, fontstyle='italic')
        
        self.save_and_close()


    def work_type_stroke_distribution(self):
        plt.figure(figsize=(11, 6))
        
        # Utilizar los mismos colores que en glucose_stroke_distribution
        colors = ['#ADD8E6', '#FFD700']
        ax = sns.countplot(x='work_type', hue='stroke', data=self.df, palette=colors)

        # Título y etiquetas de los ejes
        ax.set_title('Work Type - Stroke Distribution', fontsize=14, fontweight='bold')
        ax.set_xlabel('Work Type', fontstyle='italic', fontsize=10)
        ax.set_ylabel('Number of People',  fontstyle='italic', fontsize=10)

        # Leyenda
        ax.legend(fontsize='10',labels=['Non Stroke', 'Stroke'])

        # Estilo de los ejes y el fondo
        sns.despine(trim=True, left=True)

        # Añadir líneas de fondo intermitentes en el eje horizontal
        ax.yaxis.grid(color='gray', linestyle='--', linewidth=0.5)

        self.save_and_close()

    def marriage_glucose_relation(self):
            plt.figure(figsize=(12, 6))
            
            # Utilizar un KDE plot en lugar de un boxplot
            sns.kdeplot(data=self.df, x='avg_glucose_level', hue='ever_married', fill=True, common_norm=False, palette='pastel')
            
            plt.title('Marriage - Average Glucose Level Relation', fontweight='bold', fontsize=14)
            plt.xlabel('Average Glucose Level', fontstyle='italic', fontsize=10)
            plt.ylabel('Density', fontstyle='italic', fontsize=10)
            
            # Añadir líneas de fondo intermitentes en el eje horizontal
            plt.gca().yaxis.grid(color='gray', linestyle='--', linewidth=0.5)
            
            # Personalizar la apariencia de los cuadros
            sns.despine(trim=True, left=True)

            # Añadir leyenda con etiquetas y ajustar tamaño
            labels = {0: 'Married', 1: 'Not married'}
            legend_labels = [plt.Line2D([0], [0], marker='o', color='w', label=labels[i], 
                                        markerfacecolor=sns.color_palette('pastel')[i], markersize=8) for i in labels]
            
            plt.legend(handles=legend_labels, loc='upper right', bbox_to_anchor=(1, 1), fontsize=10)
            
            self.save_and_close()


    def age_stroke_rate_lineplot(self):
        # Configurar el estilo de los gráficos de Seaborn
        sns.set(style="whitegrid")

        # Crear la figura y los ejes
        fig, ax = plt.subplots(figsize=(12, 6))

        # Calcular la tasa de accidentes cerebrovasculares por grupo de edad
        age_groups = self.df['age_cat'].unique()
        stroke_rate = []
        for age_group in age_groups:
            subset = self.df[self.df['age_cat'] == age_group]
            stroke_rate.append(subset['stroke'].mean())

        # Invertir el orden de los grupos de edad
        age_groups = age_groups[::-1]
        stroke_rate = stroke_rate[::-1]

        # Crear el gráfico de líneas
        sns.lineplot(x=age_groups, y=stroke_rate, color='#0f4c81', ax=ax, marker='o')

        # Añadir líneas de fondo intermitentes en el eje horizontal
        ax.yaxis.grid(color='gray', linestyle='--', linewidth=0.5)

        # Personalizar la apariencia de los cuadros
        sns.despine(trim=True, left=True)

        # Añadir etiquetas al gráfico
        ax.set_title('Stroke Rate by Age Group', fontweight='bold', fontsize=14)
        ax.set_xlabel('Age Group', fontstyle='italic', fontsize=10)
        ax.set_ylabel('Stroke Rate', fontstyle='italic', fontsize=10)

        # Guardar y cerrar el gráfico
        self.save_and_close()

    def marriage_bmi_relation(self):
        # Configurar el estilo de los gráficos de Seaborn
        sns.set(style="whitegrid")

        # Configurar el fondo
        background_color = '#f6f5f5'

        # Crear la figura y los ejes
        fig, ax = plt.subplots(figsize=(12, 6), facecolor=background_color)
        ax.set_facecolor(background_color)

        # Crear el gráfico de densidad de kernel (kdeplot)
        sns.kdeplot(data=self.df, x='bmi', hue='ever_married', fill=True, common_norm=False, palette='Set2', ax=ax)

        # Añadir líneas de fondo intermitentes en el eje horizontal
        ax.yaxis.grid(color='gray', linestyle='--', linewidth=0.5)

        # Personalizar la apariencia de los cuadros
        sns.despine(trim=True, left=True)

        # Añadir leyenda con etiquetas y ajustar tamaño
        labels = {0: 'Not Married', 1: 'Married'}
        legend_labels = [plt.Line2D([0], [0], marker='o', color='w', label=labels[i], 
                                    markerfacecolor=sns.color_palette('Set2')[i], markersize=8) for i in labels]
        
        plt.legend(handles=legend_labels, loc='upper right', bbox_to_anchor=(1, 1), fontsize=10)

        # Añadir etiquetas al gráfico
        ax.set_title('Marriage - BMI Relation', fontweight='bold', fontsize=14)
        ax.set_xlabel('BMI', fontstyle='italic', fontsize=10)
        ax.set_ylabel('Density', fontstyle='italic', fontsize=10)

        # Guardar y cerrar el gráfico
        self.save_and_close()

    def correlation_heatmap(self):
        # Seleccionar solo las columnas numéricas
        numeric_columns = self.df.select_dtypes(include=['number']).columns
        numeric_df = self.df[numeric_columns]

        # Configurar el estilo de los gráficos de Seaborn
        sns.set(style="white")

        # Calcular la matriz de correlación
        correlation_matrix = numeric_df.corr()

        # Crear la figura y los ejes
        fig, ax = plt.subplots(figsize=(12, 9))

        # Crear el heatmap de correlación
        sns.heatmap(correlation_matrix, annot=True, cmap="Blues", fmt=".2f", linewidths=.35, ax=ax)

        # Ajustar las etiquetas de los ejes y el título
        ax.set_title('Correlation Heatmap', fontweight='bold', fontsize=16)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right', fontsize=7.5)
        ax.set_yticklabels(ax.get_yticklabels(), fontsize=7)

        # Ajustar el título y guardar el gráfico
        ax.set_title('Correlation Heatmap', fontweight='bold', fontsize=14)
        self.save_and_close()

    def overall_health_pie_chart(self):
        # Generate a pie chart for 'overall_health'
        health_counts = self.df['overall_health'].value_counts()

        # Colors for the pie chart
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

        # Explode the 'Very Good' slice for emphasis
        explode = [0, 0, 0, 0.1, 0]

        # Create pie chart
        plt.figure(figsize=(8, 8))
        plt.pie(health_counts, labels=health_counts.index, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode, shadow=True, wedgeprops={'edgecolor': 'black'})

        # Draw circle in the center
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)

        # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.tight_layout()

        # Set the title
        plt.title('Distribution of Overall Health')

        # Save the pie chart to the PDF
        self.save_and_close()