import pandas as pd
import numpy as np
import graphviz
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import metrics

data = pd.read_csv("datasets/dataset.csv", index_col=0)

"""
Balancing the dataset reduces the accuracy for increases in precision and recall (worth?)

Unbalanced:
              precision    recall  f1-score   support

         0.0       0.91      0.99      0.95     45968
         1.0       0.57      0.09      0.15      4768

    accuracy                           0.91     50736
   macro avg       0.74      0.54      0.55     50736
weighted avg       0.88      0.91      0.88     50736

Balanced:
              precision    recall  f1-score   support

         0.0       0.79      0.72      0.75      4818
         1.0       0.74      0.80      0.77      4740

    accuracy                           0.76      9558
   macro avg       0.76      0.76      0.76      9558
weighted avg       0.76      0.76      0.76      9558
"""
pos_sample = data[data["HeartDiseaseorAttack"] == 1]
neg_sample = data[data["HeartDiseaseorAttack"] == 0].sample(n=len(pos_sample))
data = pd.concat([pos_sample, neg_sample], ignore_index=True)
data = data.sample(frac=1)

target = data["HeartDiseaseorAttack"]
features = data.drop("HeartDiseaseorAttack", axis=1)

features_train, features_test, target_train, target_test = train_test_split(
    features, target, test_size=0.2, random_state=42
)

classifier = tree.DecisionTreeClassifier(
    max_depth=9, min_samples_leaf=4, random_state=42, criterion="entropy"
)
classifier.fit(features_train, target_train)
result = classifier.predict(features_test)
matrix = metrics.confusion_matrix(target_test, result)

print("Confusion matrix")
print(matrix)
print(metrics.classification_report(target_test, result))

importance = pd.DataFrame(
    {
        "feature": features_train.columns,
        "importance": np.round(classifier.feature_importances_, 3),
    }
)
importance.sort_values("importance", ascending=False, inplace=True)
print(importance)

dot_data = tree.export_graphviz(
    classifier,
    out_file=None,
    feature_names=features_train.columns,
    filled=True,
    proportion=True,
    rounded=True,
    max_depth=4,
)
graph = graphviz.Source(dot_data)
graph.format = "png"
graph.render("tree")
