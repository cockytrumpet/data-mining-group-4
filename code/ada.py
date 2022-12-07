import pickle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import metrics
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split

data = pd.read_csv("datasets/dataset.csv", index_col=0)

target = data["HeartDiseaseorAttack"]
features = data.drop("HeartDiseaseorAttack", axis=1)

features_train, features_test, target_train, target_test = train_test_split(
    features, target, test_size=0.2, random_state=42
)

classifier = AdaBoostClassifier()
classifier.fit(features_train, target_train)
result = classifier.predict(features_test)
matrix = metrics.confusion_matrix(target_test, result)

# save matrix to png
names = ["True Negative", "False Positive", "False Negative", "True Positive"]
counts = [f"{x:0.0f}" for x in matrix.flatten()]
percents = [f"{x:.2%}" for x in matrix.flatten() / np.sum(matrix)]
labels = [f"{n}\n{c}\n{p}" for n, c, p in zip(names, counts, percents)]
labels = np.asarray(labels).reshape(2, 2)
plt.figure(figsize=(4, 4))
pretty_matrix = sns.heatmap(matrix, annot=labels, fmt="")
pretty_matrix.set(title="AdaBoost")
pretty_matrix.set(xlabel="Predicted", ylabel="Actual")
plt.savefig("results/ada/ada_matrix")

# print stats

with open("results/ada/ada_stats.txt", "w") as f:
    f.write(metrics.classification_report(target_test, result))
    f.write("\n")

pickle.dump(classifier, open("models/ada.model", "wb"))

# do it all again with the balanced dataset

data = pd.read_csv("datasets/dataset_balanced.csv", index_col=0)

target = data["HeartDiseaseorAttack"]
features = data.drop("HeartDiseaseorAttack", axis=1)

features_train, features_test, target_train, target_test = train_test_split(
    features, target, test_size=0.2, random_state=42
)

classifier = AdaBoostClassifier()
classifier.fit(features_train, target_train)
result = classifier.predict(features_test)
matrix = metrics.confusion_matrix(target_test, result)

# save matrix to png
names = ["True Negative", "False Positive", "False Negative", "True Positive"]
counts = [f"{x:0.0f}" for x in matrix.flatten()]
percents = [f"{x:.2%}" for x in matrix.flatten() / np.sum(matrix)]
labels = [f"{n}\n{c}\n{p}" for n, c, p in zip(names, counts, percents)]
labels = np.asarray(labels).reshape(2, 2)
plt.figure(figsize=(4, 4))
pretty_matrix = sns.heatmap(matrix, annot=labels, fmt="")
pretty_matrix.set(title="AdaBoost balanced")
pretty_matrix.set(xlabel="Predicted", ylabel="Actual")
plt.savefig("results/ada/ada_balanced_matrix")

# print stats

with open("results/ada/ada_balanced_stats.txt", "w") as f:
    f.write(metrics.classification_report(target_test, result))
    f.write("\n")

pickle.dump(classifier, open("models/ada_balanced.model", "wb"))
