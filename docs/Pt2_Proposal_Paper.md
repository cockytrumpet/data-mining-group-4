### Problem Statement and Motivation

Heart disease is the leading cause of death for men, women, and people of most racial and ethnic groups in the United States. About 697,000 people in the United States died from heart disease in 2020—that’s 1 in every 5 deaths. Heart disease cost the United States about $229 billion each year from 2017 to 2018.3. This includes the cost of health care services, medicines, and lost productivity due to death. (citation: https://www.cdc.gov/heartdisease/facts.htm)

The Behavioral Risk Factor Surveillance System (BRFSS) is the nation’s premier system of health-related telephone surveys that collect state data about U.S. residents regarding their health-related risk behaviors, chronic health conditions, and use of preventive services. Established in 1984 with 15 states, BRFSS now collects data in all 50 states as well as the District of Columbia and three U.S. territories. BRFSS completes more than 400,000 adult interviews each year, making it the largest continuously conducted health survey system in the world. (citation: https://www.cdc.gov/brfss/index.html)

Using data from the BRFSS, we intend to determine which risk factors are the strongest indicators of heart disease and look for correlations between risk factors. We will then attempt to predict heart disease in a patient given the presence of indicators using <insert smart sounding words about classification/ML here>

### Literature Review
Look into what previous work has been done with both this data and other data that is closely related. Would be pretty easy as there is plenty of studies regarding heart disease as it connects to many different interesting attributes

Fortunatly, heart disease and heart disease indicators are a well researched topic. Unfortnatly, heart disease is a largely prevelant disease that affects many people world wide. Proposing the question of "how do we better predict heart disease?" helps us narrow down what work we can look at for background informtaion and inspiration in this exploratory study.

### Proposed Work
- What needs to be done to the data in the first place
	- Seems pretty cleaned, will update this shortly
- Derive bins from variables: BMI, MentHlth, PhysHlth, Age(?)
- What are we doing that is different that what has been previusly done based on what we found in the literature review, or how and why we are replicating certain things
	- Will likely be a blend of the two as It might be hard to do something not explored on such a well researched topic. Why we believe the replication is interesting, or important could be something to talk about here.

### Data Set

The Behavioral Risk Factor Surveillance System (BRFSS) is a health-related telephone survey that is collected annually by the CDC. This dataset is reduced and cleaned from the responses given in 2015. It can be found at https://www.kaggle.com/datasets/alexteboul/heart-disease-health-indicators-dataset. Our working copy as well as the version containing derived attributes will be available at https://github.com/cockytrumpet/data-mining-group-4.


The data set contains 253680 objects, each with 22 attributes.

| Attribute | Description | Type | Requires Data Binning |
|-|-|-|-|
HeartDiseaseorAttack | Heart disease or attack | Binary | No |
HighBP | High blood pressure | Binary | No |
HighChol | High cholesterol | Binary | No |
CholCheck | Cholesterol check < 5 years | Binary | No |
BMI | Body Mass Index | Ordinal | Yes |
Smoker | >99 cigarettes ever smoked | Binary | No |
Stroke | Ever had stroke | Binary | No |
Diabetes | Has diabetes | Binary | No |
PhysActivity | Pysical activity in past 30 days | Binary | No |
Fruits | Consume fruit >= 1 time per day | Binary | No |
Veggies | Consume vegetables >= 1 time per day | Binary | No |
HvyAlcoholConsump | Men: >14 drinks/week, Women: >7 drinks/week | Binary | No |
AnyHealthcare | Health coverage | Binary | No |
NoDocbcCost | Didn't seek health care <12 months due to cost | Binary | No |
GenHlth | General health | Ordinal | No |
MentHlth | Days in past 30 days where mental health was poor | Ordinal | Yes |
PhysHlth | Days in past 30 days where physical health was poor | Ordinal | Yes |
DiffWalk | Difficulty walking or climbing stairs | Binary | No |
Sex | Sex | Binary | No |
Age | Age category | Ordinal | Yes |
Education | Highest grade or year of school completed | Ordinal | No |
Income | Annual household income | Ordinal | No |



### Evaluation Methods
I am a bit confused as to what the goal here is, what metrics and existing solutiosn exist for this data? Or what models are we using to evaluate the data?

How can we evaluate the results of our analysis?
- Is our trained model able to make accurate predictions?
- How do our results compare to results seen in the literature?
- I think the app would be an extension to bullet 1. Once we have a useful model we could show the real world application of it. For me, this falls into the category of "would be nice to have" given we get the rest of the project to a presentable state with time to spare.
- This could be where the full stack app maybe comes in, as long as we see that as a reasonable use of time in this class. Having an interactive tool that reports information back to users as well as generates its own data could be interesting way to evaluate the fidnings in the data that we find as compared to the (minimal albeit) data we could generate with the small web app. My main concern is how many new potential issues we could be potentially introducing to a relatively simple exploration project. Would have to gauge group interest level in this because it might just lead to more headaches than worth it at this point in everyones degree progress.

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
How can we roadmap this project? Looking ahead, coordinate due dates with certain things we can reasonable achieve in that time.

- November 01: Data cleaning and attribute binning completed
- October 31:
- November 07: 
- November 14:
- November 21:
- **November 28: Project Part 3 Due – Progress Report**
- November 28: Report final revisions, Code clean-up
- December 05: Presentation final revisions
- **December 08: Project Parts 4-7 Due - Report, Code, Presentation, Evaluations**

