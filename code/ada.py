import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pickle

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

print("Confusion matrix")
print(matrix)
print(metrics.classification_report(target_test, result))

pickle.dump(classifier, open("models/ada.model", "wb"))
