# data-mining-group-4

### **Title:** Heart Disease Prediciton and Risk Factors

### **Team members:** Adam Fowler, Tyler Sanchez, Jacob Unger

### **Description:** Using data from the Behavioral Risk Factor Surveillance System (BRFSS), determine which risk factors are the strongest indicators of heart disease. Look for correlations between risk factors. Attempt to predict heart disease in a patient given the presence of indicators.

### **Prior Work:** This is a popular dataset on Kaggle with a variety of prior work. Our goal will be an independent analysis with results being verified by prior work.

Sample of prior work:
| Title | URL |
|-------|-----|
| Heart Disease Fastai with TabularPandas | [https://www.kaggle.com/code/stpeteishii/heart-disease-fastai-with-tabularpandas](https://www.kaggle.com/code/stpeteishii/heart-disease-fastai-with-tabularpandas) |
| Heart Disease - Binary Classification | [https://www.kaggle.com/code/murattademir/heart-disease-binary-classification](https://www.kaggle.com/code/murattademir/heart-disease-binary-classification) |
| Heart Disease Indication (PCA, Classifier & CNN) | [https://www.kaggle.com/code/sohaelshafey/heart-disease-indication-pca-classifier-cnn](https://www.kaggle.com/code/sohaelshafey/heart-disease-indication-pca-classifier-cnn) |
| Nueral Network Regression VS Sklearn Algorithms | [https://www.kaggle.com/code/abohelal/nueral-network-regression-vs-sklearn-algorithms](https://www.kaggle.com/code/abohelal/nueral-network-regression-vs-sklearn-algorithms) |


### **Dataset**
- Heart Disease Health Indicators Dataset
- [https://www.kaggle.com/datasets/alexteboul/heart-disease-health-indicators-dataset](https://www.kaggle.com/datasets/alexteboul/heart-disease-health-indicators-dataset)
- The dataset and our additions will be stored at [https://github.com/cockytrumpet/data-mining-group-4](https://github.com/cockytrumpet/data-mining-group-4)

### **Proposed work**
- Data cleaning
   -	Look for discrepancies in the data, this will insure the accuracy of the data and ensure variables all line up and are in the same format across all entries.
   -  	For missing values, we will use a universal constant where ever that may be necessary. Either a numerical value or a ‘Unknown’ label. 
   -	In order to clean up noise, use outlier analysis to prune and smooth the data. Regression will be used to see if there are related variables. 

- Data preprocessing
  - Investigate the believability and interpretability of the data as well as its accuracy and consistency. This will insure the data can be trusted and understood.
  - Perform data reduction and data transformation in order to aid in analysis.

- Data integration
  - Perform correlation analysis to see if there is anything that we can use to predict heart disease based on the attributes that are given. 
  - Ensure attention is paid to conflict detection and make sure to resolve issues that arise.


- Tools to be used 
  - python/R
  - pandas - dataset manipulation
  - matplotlib/seaborn - visualization
  - scikit - analysis/classification


### **Questions we aim to Answer**
1. Are we able to accurately model a way to predict heart disease based on the attributes that are common indicators of poor coronary health?
	- Through the use of various models, aiming to accuratly plug in a patients data to our models and tell them their risk for heart disease
2. Which of these attributes are the most important factors when determining risk of Coronary heart disease?
	- Narrowing in ok key attributes to boil down the important information for health decisions
3. How can we make this information more approachable and digestible to the general public?
	- Through the use of a simple web app, make this information accessible to more people.

### **Evaluation**
- Sample to create a testing dataset. 
- Test the efficacy of our model.
- Present information to people outside of the creation process.
- Allow people to use the model and determine if it helped them better understand their risk.

<br>

### **Application of the information gained**
One of our original goals was to ake this information more accessible to the general public, adn we achieved that by creating a small web application that is based on the models we found to be best.
Using Flask, we were able to tie in the model, using the 7 factors that were statistically determined to be high influence on the outcome, the user inputs those answers into a form, which is run through the model and a binary of high or low risk is determined. Setting out, we ideally wanted to return a percentage but unfortunatly the model that was best suited for this application based on our data returned a binary. Moving forward, tailoring information based on the user input to provide an even better answer would be ideal in making htis information more approachable and easier to understand. 


### **Link to presentation**
https://docs.google.com/presentation/d/1csEElXiHB4GJ2vBgSL2gKtzkgLuavpISGrliMVuojoM/edit?usp=sharing

### **Link to video presentation**
https://youtu.be/zSHCQT4rzjY

