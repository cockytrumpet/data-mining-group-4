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

Confusion matrix
[[45480   488]
 [ 4273   495]]
              precision    recall  f1-score   support

         0.0       0.91      0.99      0.95     45968
         1.0       0.50      0.10      0.17      4768

    accuracy                           0.91     50736
   macro avg       0.71      0.55      0.56     50736
weighted avg       0.88      0.91      0.88     50736

              feature  importance
11            GenHlth       0.347
14                Age       0.210
4              Stroke       0.108
13                Sex       0.066
1            HighChol       0.057
0              HighBP       0.053
16             Income       0.022
3              Smoker       0.020
15          Education       0.018
20       Diabetes_bin       0.018
12           DiffWalk       0.016
17            BMI_bin       0.015
18       MentHlth_bin       0.010
19       PhysHlth_bin       0.010
6              Fruits       0.007
10        NoDocbcCost       0.006
8   HvyAlcoholConsump       0.004
7             Veggies       0.004
5        PhysActivity       0.004
9       AnyHealthcare       0.003
2           CholCheck       0.003
```
