
# Correlation map

# Ver si el marriage_status influye en las enfermedades:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

# Cargar el conjunto de datos
df = pd.read_csv("outputs/cleaned_dataset.csv")

# Seleccionar las columnas relevantes para el análisis
columns_of_interest = ["ever_married", "heart_disease", "hypertension", "stroke"]
selected_data = df[columns_of_interest]

# Crear una tabla de contingencia
contingency_table = pd.crosstab(selected_data["ever_married"], selected_data["heart_disease"])

# Realizar el test chi-cuadrado
chi2, p, _, _ = chi2_contingency(contingency_table)

# Imprimir resultados
print(f"Chi2 Value: {chi2}")
print(f"P-value: {p}")

# Interpretar los resultados
alpha = 0.05
print(f"\nSignificance level: {alpha}")
if p < alpha:
    print("Hay evidencia estadística para rechazar la hipótesis nula.")
    print("La presencia de enfermedades cardíacas está asociada con el estado civil.")
else:
    print("No hay evidencia estadística para rechazar la hipótesis nula.")
    print("No hay asociación significativa entre la presencia de enfermedades cardíacas y el estado civil.")

# Visualizar la tabla de contingencia como un gráfico de barras apiladas
plt.figure(figsize=(10, 6))
sns.barplot(x=contingency_table.index, y=contingency_table[1], label="Con enfermedad")
sns.barplot(x=contingency_table.index, y=contingency_table[0], bottom=contingency_table[1], label="Sin enfermedad")

# Añadir etiquetas y leyenda
plt.title("Relación entre Estado Civil y Enfermedades Cardíacas")
plt.xlabel("Estado Civil")
plt.ylabel("Número de Personas")
plt.legend(title="Enfermedad")

# Mostrar el gráfico
plt.show()