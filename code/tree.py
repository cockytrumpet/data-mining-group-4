import pandas as pd
import numpy as np
import graphviz
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import metrics


def make_tree(data, matrix_title, output_file):
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

    # save matrix to png
    names = ["True Negative", "False Positive", "False Negative", "True Positive"]
    counts = [f"{x:0.0f}" for x in matrix.flatten()]
    percents = [f"{x:.2%}" for x in matrix.flatten() / np.sum(matrix)]
    labels = [f"{n}\n{c}\n{p}" for n, c, p in zip(names, counts, percents)]
    labels = np.asarray(labels).reshape(2, 2)
    plt.figure(figsize=(4, 4))
    pretty_matrix = sns.heatmap(matrix, annot=labels, fmt="")
    pretty_matrix.set(title=matrix_title)
    pretty_matrix.set(xlabel="Predicted", ylabel="Actual")
    plt.savefig(f"{output_file}_matrix")

    # print stats
    importance = pd.DataFrame(
        {
            "feature": features_train.columns,
            "importance": np.round(classifier.feature_importances_, 3),
        }
    )
    importance.sort_values("importance", ascending=False, inplace=True)
    print(f"{matrix_title}")
    print(metrics.classification_report(target_test, result))
    print(importance)

    # save decision tree as png
    dot_data = tree.export_graphviz(
        classifier,
        out_file=None,
        feature_names=features_train.columns,
        filled=True,
        proportion=True,
        rounded=True,
        max_depth=3,
        rotate=True,
    )
    graph = graphviz.Source(dot_data)
    graph.format = "png"
    graph.render(output_file)


data_original = pd.read_csv("datasets/dataset.csv", index_col=0)

pos_sample = data_original[data_original["HeartDiseaseorAttack"] == 1]
neg_sample = data_original[data_original["HeartDiseaseorAttack"] == 0].sample(
    n=len(pos_sample)
)
data_balanced = pd.concat([pos_sample, neg_sample], ignore_index=True)
data_balanced = data_balanced.sample(frac=1)

make_tree(data_original, "Original", "tree")
make_tree(data_balanced, "Balanced", "tree_balanced")
