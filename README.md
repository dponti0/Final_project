# Final project 

The purpose of this document is to further explain what my repository does, defining the aim of the study, ilustrating how to run it and to extract some final conclusions.

## Project Overview

This repository contains the final project developed as part of the Advanced Python course at ESADE. The main objective of this project was to apply the concepts and techniques covered throughout the course to a specific DataFrame obtained from Kaggle. The project involves data cleaning, initial exploration, parallel execution of various scripts, and drawing conclusions based on the analysis performed.

## Requirements & Functionality

The project's requirements are listed in the "requirements.txt" file. 

Despite the fact that the Makefile should automatically pip install them, I add the code here just in case.

To install the required libraries, use the following command:

    pip install -r requirements.txt

*Compatibility Note:* To guarantee compatibility with versions earlier than Python 3.3 and with older versions, an `__init__.py` file has been included.

**The project is structured as follows:**
    
1. **Data Cleaning:**
   To start, execute the data cleaning script with the appropriate input and output paths:
        
        python scripts/data_cleaning.py -i dataset/healthcare_dataset.csv -o outputs/cleaned_dataset.csv

This script utilizes click commands and saves the cleaned dataset in the "outputs" folder for further analysis.

2. **Initial Exploration:**
Execute the script for initial data exploration to obtain relevant statistical information about the dataset:

        python scripts/data_exploration.py

The results of this exploration will be saved in the "outputs" folder as a .txt file.

3. **Main Script Execution:**
Run the main project script, which concurrently executes the marriage study, predictive (regression) script, and univariate/multivariate analyses:

        python scripts/main_project_script.py

This will generate PDF files containing the results of the marriage study and numerical analysis in the "outputs" folder. Additionally, the predictions for strokes will be saved in a .txt file in the same folder.


*After all the code was correctly elaborated and run, we can move on with code formatting. linting (2 linting formats were used) and unit testing.*

## Code Formatting

Black was used to format the code. You may want to run the Black instance using the following code:

        black tests
        black scripts

## Code Linting

Flake8 was used to lint the code. You may want to run the flake8 instance via the following code:

        flake8 tests
        flake8 scripts

Pylint was another tool used to lint the code. You may want to run it using the following code:

        pylint scripts
        pylint tests

The results obtained running pylint, after careful consideration and correcting the code as much as possible, were the following ones:
- *Scripts*: Your code has been rated at 8.85/10 
- *Tests*: Your code has been rated at 9.32/10 

## Unit testing

Pytest has been used to check wether all tests pass or not and to correct some minor errors. The code to properly run it is the following one:

        pytest tests

This command will execute all the tests in the tests directory.
All the tests should pass, nevertheless, some warnings may arise. Those are the actual results:
- *33 passed, 34 warnings in 2.25s*

## Conclusions

Upon analysis of the dataset, several observations were made:

- The dataset has minimal missing or irrelevant data.
- A majority of individuals fall within the adult to elderly age range, are married, and predominantly female (60%) compared to males (40%).
- Few individuals smoke, and only a small percentage have experienced strokes, hypertension, or heart disease.

However, notable observations include elevated BMI and glucose levels for many individuals, suggesting a study conducted in a developed country, possibly the USA. The "overall health" column, created through feature engineering, indicates that a small percentage have good (10%) or very good (17.7%) health.

Correlations were observed between glucose levels and smoking habits, with age influencing the likelihood of overweight and strokes, the latter being the variable most correlated with age.

The type of occupation also shows a correlation with stroke risk, with individuals in the private sector being more prone than those in government roles or children.

Interestingly, marriage seems to negatively influence health, as married individuals are more likely to experience heart disease, higher glucose levels, and increased BMI compared to single individuals, supported by a chi-squared test.

In conclusion, age emerges as the most significant factor in health issues. However, glucose levels, often leading to high BMI, stand out as the second most correlated variable, emphasizing the importance of maintaining low blood sugar levels to prevent diseases.



*Final notes*
- *Visualizing the pdf outputs directly from github web tends to take a bit more time.*
- *My anaconda environment is advancedpython, which I active using the following code:*
        conda activate advancedpython
- *I did not erase the outputs just in case you previously wanted to visualize them, by running the code you should get the same results.*
- *Debugging was employed only once to enhance the smooth execution of the code.*
- *Some errors arise when running the main_script, however, they are future warning errors which do not directly impact the final output.*
