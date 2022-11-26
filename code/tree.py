import pandas as pd
import numpy as np
import graphviz
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import metrics

data = pd.read_csv("datasets/dataset.csv", index_col=0)

target = data["HeartDiseaseorAttack"]
features = data.drop("HeartDiseaseorAttack", axis=1)

features_train, features_test, target_train, target_test = train_test_split(
    features, target, test_size=0.2, random_state=42
)

classifier = tree.DecisionTreeClassifier(max_depth=10, random_state=42, criterion='entropy')
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

dot_data = tree.export_graphviz(classifier, out_file=None, feature_names=features_train.columns, filled=True, proportion=True, rounded=True, max_depth=4)
graph = graphviz.Source(dot_data)
graph.format = 'png'
graph.render("tree")
