import pickle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

data = pd.read_csv("datasets/dataset_balanced.csv", index_col=0)

target = data["HeartDiseaseorAttack"]
features = data.drop("HeartDiseaseorAttack", axis=1)

features_train, features_test, target_train, target_test = train_test_split(
    features, target, test_size=0.2, random_state=42
)

classifier = MLPClassifier(alpha=1, max_iter=1000)
classifier.fit(features_train, target_train)
result = classifier.predict(features_test)
matrix = metrics.confusion_matrix(target_test, result)

# save model
pickle.dump(classifier, open("models/mlp.model", "wb"))

# save matrix to png
names = ["True Negative", "False Positive", "False Negative", "True Positive"]
counts = [f"{x:0.0f}" for x in matrix.flatten()]
percents = [f"{x:.2%}" for x in matrix.flatten() / np.sum(matrix)]
labels = [f"{n}\n{c}\n{p}" for n, c, p in zip(names, counts, percents)]
labels = np.asarray(labels).reshape(2, 2)
plt.figure(figsize=(4, 4))
pretty_matrix = sns.heatmap(matrix, annot=labels, fmt="")
pretty_matrix.set(title="MLP")
pretty_matrix.set(xlabel="Predicted", ylabel="Actual")
plt.savefig("results/mlp/mlp_matrix")

# print stats
with open("results/mlp/mlp_stats.txt", "w") as f:
    f.write(metrics.classification_report(target_test, result))
