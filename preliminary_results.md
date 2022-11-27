# Naive Bayes
```
Confusion matrix
[[38994  6974]
 [ 2163  2605]]
              precision    recall  f1-score   support

         0.0       0.95      0.85      0.90     45968
         1.0       0.27      0.55      0.36      4768

    accuracy                           0.82     50736
   macro avg       0.61      0.70      0.63     50736
weighted avg       0.88      0.82      0.85     50736

```
# AdaBoost
```
Confusion matrix
[[45352   616]
 [ 4061   707]]
              precision    recall  f1-score   support

         0.0       0.92      0.99      0.95     45968
         1.0       0.53      0.15      0.23      4768

    accuracy                           0.91     50736
   macro avg       0.73      0.57      0.59     50736
weighted avg       0.88      0.91      0.88     50736

```
# Multi-layer Perceptron
```
Confusion matrix
[[45920    48]
 [ 4641   127]]
              precision    recall  f1-score   support

         0.0       0.91      1.00      0.95     45968
         1.0       0.73      0.03      0.05      4768

    accuracy                           0.91     50736
   macro avg       0.82      0.51      0.50     50736
weighted avg       0.89      0.91      0.87     50736

```
# Decision Tree
```

Confusion Matrix - Original
              precision    recall  f1-score   support

         0.0       0.91      0.99      0.95     45968
         1.0       0.57      0.09      0.15      4768

    accuracy                           0.91     50736
   macro avg       0.74      0.54      0.55     50736
weighted avg       0.88      0.91      0.88     50736

              feature  importance
11            GenHlth       0.372
14                Age       0.294
0              HighBP       0.075
4              Stroke       0.070
13                Sex       0.062
1            HighChol       0.056
3              Smoker       0.013
16             Income       0.012
20       Diabetes_bin       0.012
12           DiffWalk       0.010
15          Education       0.005
17            BMI_bin       0.004
18       MentHlth_bin       0.003
19       PhysHlth_bin       0.003
9       AnyHealthcare       0.002
7             Veggies       0.002
5        PhysActivity       0.002
10        NoDocbcCost       0.002
8   HvyAlcoholConsump       0.001
6              Fruits       0.001
2           CholCheck       0.001

Confusion Matrix - Balanced
              precision    recall  f1-score   support

         0.0       0.78      0.72      0.75      4825
         1.0       0.73      0.80      0.76      4733

    accuracy                           0.76      9558
   macro avg       0.76      0.76      0.76      9558
weighted avg       0.76      0.76      0.76      9558

              feature  importance
11            GenHlth       0.376
14                Age       0.295
0              HighBP       0.061
1            HighChol       0.058
13                Sex       0.058
4              Stroke       0.048
16             Income       0.018
12           DiffWalk       0.015
3              Smoker       0.014
15          Education       0.010
20       Diabetes_bin       0.009
17            BMI_bin       0.007
6              Fruits       0.005
18       MentHlth_bin       0.005
10        NoDocbcCost       0.004
7             Veggies       0.003
5        PhysActivity       0.003
2           CholCheck       0.003
19       PhysHlth_bin       0.003
8   HvyAlcoholConsump       0.002
9       AnyHealthcare       0.001
```
