### Problem Statement and Motivation

Heart disease is the leading cause of death for men, women, and people of most racial and ethnic groups in the United States. About 697,000 people in the United States died from heart disease in 2020—that’s 1 in every 5 deaths. Heart disease cost the United States about $229 billion each year from 2017 to 2018. This includes the cost of health care services, medicines, and lost productivity due to death. (citation: https://www.cdc.gov/heartdisease/facts.htm)

The Behavioral Risk Factor Surveillance System (BRFSS) is the nation’s premier system of health-related telephone surveys that collect state data about U.S. residents regarding their health-related risk behaviors, chronic health conditions, and use of preventive services. Established in 1984 with 15 states, BRFSS now collects data in all 50 states as well as the District of Columbia and three U.S. territories. BRFSS completes more than 400,000 adult interviews each year, making it the largest continuously conducted health survey system in the world. (citation: https://www.cdc.gov/brfss/index.html)

Using data from the BRFSS, we intend to determine which risk factors are the strongest indicators of heart disease and look for correlations between risk factors. We will then attempt to predict heart disease in a patient given the presence of indicators using various techniques of classification.


### Literature Review (Needs Proper Citations)

Fortunately, heart disease and heart disease indicators are a well researched topic. Unfortunately, heart disease is a largely prevalent disease that affects many people world wide. Proposing the question of "how do we better predict heart disease?" helps us narrow down what work we can look at for background information and inspiration in this exploratory study. The prediction of heart disease has far reaching implication on better individual health and societal health, as cardiovascular disease is the biggest cause of morbidity and mortality. To determine where the current research stands, we looked at papers under search terms such as "heart disease prediction", "predictive factors of heart disease", and "health indicators heart disease". 

In one study, by authors Tavia Gordan; William P. Castelli, MD; Marthana C. Hjortland, PhD; et al, titled 'Predicting Coronary Heart Disease in Middle-Aged and Older Persons'. In this study, 2470 people, 1025 men and 1445 women, of ages ranging from 49 to 82 years, were screened in this study. Using factors such as cholesterol in the high and low density lipoproteins, systolic blood pressure, left ventricular hypertrophy and diabetes, they were able to generate a function that could be used to classify the chance of coronary heart disease. This in turn found that 25% of men in the highest decile, and 37% of women in the highest decile had coronary heart disease for the sample. This model fit for each specific age group and well as was at least as good as the coronary heart disease risk profile that is generally used when classifying risk for those within a younger population. This study was certainly framed through a more medical perspective, focusing on quantifying health indicators and factors that are obtained through specific medical measurements, whereas out data focuses on binary and largely observable health indicators.  One thing we will take away from this study is their application of the model to populations outside of their sample. This provides an interesting insight into how well the model can be applied elsewhere or if the research needs to be retuned and redone for different populations.
https://jamanetwork.com/journals/jama/article-abstract/354740


A study titled "Predicting Heart Disease at Early Stages using Machine Learning: A Survey" by authors Rahul Katarya, Polipireddy Srinivas, et al, used some similar data analysis techniques that we aim to use in our analysis, providing a good roadmap for us to look at. These modeling techniques that were used in this study were artificial neural networks, decision tree, random forest, support vector machine, naive Bayes, and k-nearest neighbor algorithm. This study heavily focused on the benefit of predicting heart disease during early stages of the development of the disease as to better focus on treatment and prevention, while also going over where the current knowledge of using machine learning in specifically heart disease stands, highlighting great information such as the various methods that are currently used, there Data Mining schemes that assist in accurate findings and future predictions, and the steps that are currently being used to get to those accurate findings. While being a shorter paper on the whole, the information included is very technical and very helpful in helping us understand how more efficient and large scale data mining and modeling operations take place, giving us vital information in how to proceed within our exploration of a heart disease prediction data set. By giving us a review of the current statistical modeling that is taking place with data that is similar to what we are working with, we know have a better idea of what modeling we may want to move foward with to get the best result given the limited working time of this project.
https://ieeexplore.ieee.org/abstract/document/9155586


Looking at the more technical aspect of studying heart disease using prediction factors, the study titled "Identification of significant features and data mining techniques in predicting heart disease" by authors Mohammad Shafenoor-Aminac, Yin KiaChiama, and Kasturi DewiVarathanb, looks at specific techniques in data mining that are common in this field of study and provides good background information for us as we move into this space. Evaluating different classification algorithms, focusing on efficient data mining techniques for heart disease predictions and determining the performance of classification models for heart disease predictions, allowed the research to develop a prediction model using the significant features of the models evaluated while using hybrid data mining techniques for the best results. These researchers evaluates k-Nearest Neighbor, Naive Bayes, Logistic Regression, Support vector Machine, Neural Network, and Vote, which is a hybrid technique blending Naive Bayes and Logistic Regression. By Identifying specific features that shined for each model and data mining technique, they aimed to improve prediction modeling for cardiovascular disease prediction. It was found that the Vote modeling technique (the blend of Naive Bayes and Logistic Regression) was the highest performer, and using the key features determined as applied to mining techniques they were able to achieve an accuracy of 87.4% in heart disease prediction as applied to their sample population. This study has lots of great in-depth information that we can leverage in determine the models we choose to use for our predictive model. While we likely wont be using a model as complicated as the Vote Model they determined to be the most accurate, choosing a model that had strong results based on the data that we are feeding it will closely follow some of the techniques that were used within this research study.
https://www.sciencedirect.com/science/article/abs/pii/S0736585318308876


### Proposed Work

The first thing that we will need to do for this section is create data bins that will be made from the variables at hand. These will look at variables like BMI, Sex, Age, Physical Health, or any of the other attributes that are listed in out data set. As for the data cleaning, it overall looks pretty well organized and complete, it will mostly be checking for any missing data and making sure that all of the data lines up with each other structurally. 

Once we create the bins from the variables, we will then analyze the bins to see if we can create a model to predict heart disease based on the different variables. For this, the best model could be a decision tree, this will run through the different variables and then hopefully be able to indicate whether or not there is a risk of heart disease. The analysis for this will be done through Python, Pandas, and R. 

Looking at past reviews, this is a very studied topic, in some ways this will be a similar study to those done in the past in the case that this will be trying to predict heart disease based on certain variables. Also when looking at prior studies, it looks like there may be similarities on strategies that we can use as a guide to analyze the data and then create a model for prediction. The difference in this project, is that additional derived attributes will be analyzed to see if it is able to find a better predictor of heart disease. 


### Data Set

The Behavioral Risk Factor Surveillance System (BRFSS) is a health-related telephone survey that is collected annually by the CDC. A sample of the survey and it's questions can be found at https://www.cdc.gov/brfss/annual_data/2015/pdf/codebook15_llcp.pdf. This dataset is reduced and cleaned from the responses given in 2015. It can be found at https://www.kaggle.com/datasets/alexteboul/heart-disease-health-indicators-dataset. Our working copy as well as the version containing derived attributes will be available at https://github.com/cockytrumpet/data-mining-group-4.


The data set contains 253680 objects, each with 22 attributes.

| Attribute | Description | Type | Requires Data Binning |
|-|-|-|-|
HeartDiseaseorAttack | Heart disease or attack | Binary | No |
HighBP | High blood pressure | Binary | No |
HighChol | High cholesterol | Binary | No |
CholCheck | Cholesterol check within last 5 years | Binary | No |
BMI | Body Mass Index | Ordinal | Yes |
Smoker | >99 cigarettes ever smoked | Binary | No |
Stroke | Ever had stroke | Binary | No |
Diabetes | Has diabetes | Binary | No |
PhysActivity | Pysical activity in past 30 days | Binary | No |
Fruits | Consume fruit >= 1 time per day | Binary | No |
Veggies | Consume vegetables >= 1 time per day | Binary | No |
HvyAlcoholConsump | Men: >14 drinks/week, Women: >7 drinks/week | Binary | No |
AnyHealthcare | Health coverage | Binary | No |
NoDocbcCost | Didn't seek health care in last 12 months due to cost | Binary | No |
GenHlth | General health | Ordinal | No |
MentHlth | Days in past 30 days where mental health was poor | Ordinal | Yes |
PhysHlth | Days in past 30 days where physical health was poor | Ordinal | Yes |
DiffWalk | Difficulty walking or climbing stairs | Binary | No |
Sex | Sex | Binary | No |
Age | Age category | Ordinal | Yes |
Education | Highest grade or year of school completed | Ordinal | No |
Income | Annual household income | Ordinal | No |



### Evaluation Methods
Ultimately, the success of our project will be determined by our ability to work with the data set. Can we create a model to make accurate predictions? Although is unlikely that we will be able to acheive the level of accuracy that was obtained from the more advanced methods shown in the literature review, if our results can mirror those results to a significant degree, that would be considered successful. 

Once the model is in place, it's efficacy can be demonstrated in a real world scenario via a user interface that allows a patients data to be entered then classified by the model.

### Tools Used
Python and R will be the main programming frameworks used for data analysis, model generation, and data visualization. Within these frameworks, packages such as Pandas will be used for dataset manipulation to prepare for processing, matplotlib, seaborn, and ggplot will be used to create visualizations of the data, and scikit will be used for analysis and classification of the data

| Tool | Source |
|-|-|
| Python | https://www.python.org/ |
| R | https://www.r-project.org/ |
| Pandas | https://pandas.pydata.org/ |
| Matplotlib | https://matplotlib.org/ |
| Seaborn | https://seaborn.pydata.org/ |
| Ggplot | https://ggplot2.tidyverse.org/ |
| Scikit | https://scikit-learn.org/stable/index.html|

### Milestones

- Oct 31: Data cleaning and attribute binning completed
- Nov 07: Preliminary analysis, classification methodologies chosen
- Nov 14: Model trained
- Nov 21: Report first draft
- **Nov 28: Project Part 3 Due – Progress Report**
- Nov 28: Report final revisions, Presentation first draft
- Dec 05: Presentation final revisions, Code clean-up
- **Dec 08: Project Parts 4-7 Due - Report, Code, Presentation, Evaluations**
