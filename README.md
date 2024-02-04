# Final project 

Explanation of what my repository does

El objetivo de este trabajo era aplicar todos los contenidos vistos a lo largo de la asignatura
de Advanced Python de ESADE en un DataFrame específico con el fin de poner en práctica los 
conocimientos adquiridos. 

En este caso, el DataFrame ha sido obtenido de Kaggle.

## Funcionamiento

Mi trabajo ha sido estructurado de la siguiente forma:
    
    1. Primero debemos ejecutar el script de data cleaning para poder proseguir con nuestro estudio
            (Dado que usamos click commands, ejecutamos el siguiente script):
    
        # python scripts/data_cleaning.py -i dataset/healthcare_dataset.csv -o outputs/cleaned_dataset.csv 

    Este script guardará el cleaned dataset en la carpeta de outputs, el cual será utilizado
    a partir de este momento.

    2. Seguidamente, deberemos run el script de la exploracion inicial, el cual incluye datos
        estadísticos relevantes sobre el dataset, para así obtener una idea inicial de él.
        El código para ejecutar este script es el siguiente:

        # python scripts/data_exploration.py 

    Los datos obtenidos al ejecutar este script serán guardados en la carpeta de outputs en
    formato .txt.

    3. Posteriormente, ejecutaremos el script principal del trabajo, el cual ejecuta paralelamente
    el marriage study script, el script predictivo (regression) y los análisis univariado y multivariado.
    Para ejecutar este archivo deberemos aplicar el siguiente código:

            # python scripts/data_exploration.py 

    Mediante esto obtendremos los respectivos pdf que incluirán los resultados tanto del marriage
    study y del análisis numérico, los cuales seran guardados también en la carpeta de outputs. Los resultados de la predicción de strokes los podremos observar en el documento .txt que se generará y guardará en la misma carpeta.



## Conclusiones




## Requirements & usage

He añadido librerias que he ido necesitando para la elaboracion del trabajo en requirements.txt

scripts --> python -i 
tests --> pthon -i
pytest
flake8 --> flake8 folder/to/lint
Pylint --> pylint folder/to/lint


Para versiones anteriores a Python 3.3 o si quieres garantizar la compatibilidad con versiones anteriores, incluye __init__.py

el df tiene irregularidad de mayúsculas y minúsculas, por tanto en el script de data cleaning se ponen todas minúsculas

# python scripts/data_cleaning.py -i dataset/healthcare_dataset.csv -o outputs/cleaned_dataset.csv

Run the black instance 

Run the flake8 cleaning instance

Run the pylint instance:
    *Scripts: Your code has been rated at 8.85/10
            pylint scripts
    *Tests: Your code has been rated at 9.32/10
            pylint tests
