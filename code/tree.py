import pickle

import graphviz
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import metrics, tree
from sklearn.model_selection import train_test_split


def make_tree(data, matrix_title, output_file):
    target = data["HeartDiseaseorAttack"]
    features = data.drop("HeartDiseaseorAttack", axis=1)

    features_train, features_test, target_train, target_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )

    classifier = tree.DecisionTreeClassifier(
        max_depth=7, min_samples_leaf=4, random_state=42, criterion="entropy"
    )
    classifier.fit(features_train, target_train)
    result = classifier.predict(features_test)
    matrix = metrics.confusion_matrix(target_test, result)

    # save model
    pickle.dump(classifier, open(f"models/{output_file}.model", "wb"))

    # save matrix to png
    names = ["True Negative", "False Positive", "False Negative", "True Positive"]
    counts = [f"{x:0.0f}" for x in matrix.flatten()]
    percents = [f"{x:.2%}" for x in matrix.flatten() / np.sum(matrix)]
    labels = [f"{n}\n{c}\n{p}" for n, c, p in zip(names, counts, percents)]
    labels = np.asarray(labels).reshape(2, 2)
    plt.figure(figsize=(4, 4))
    pretty_matrix = sns.heatmap(matrix, annot=labels, fmt="")
    pretty_matrix.set(title=f"Decision Tree {matrix_title}")
    pretty_matrix.set(xlabel="Predicted", ylabel="Actual")
    plt.savefig(f"results/tree/{output_file}_matrix")

    # print stats
    importance = pd.DataFrame(
        {
            "feature": features_train.columns,
            "importance": np.round(classifier.feature_importances_, 3),
        }
    )
    importance.sort_values("importance", ascending=False, inplace=True)

    with open(f"results/tree/{output_file}_stats.txt", "w") as f:
        f.write(metrics.classification_report(target_test, result))
        f.write("\n")
        f.write(importance.to_string())

    # save small decision tree as png
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
    graph.render(f"results/tree/{output_file}")

    # save small decision tree as png horizontal
    dot_data = tree.export_graphviz(
        classifier,
        out_file=None,
        feature_names=features_train.columns,
        filled=True,
        proportion=True,
        rounded=True,
        max_depth=3,
        rotate=False,
    )
    graph = graphviz.Source(dot_data)
    graph.format = "png"
    graph.render(f"results/tree/{output_file}_horizontal")

    # save full decision tree as png
    dot_data = tree.export_graphviz(
        classifier,
        out_file=None,
        feature_names=features_train.columns,
        filled=True,
        proportion=True,
        rounded=True,
        max_depth=7,
        rotate=True,
    )
    graph = graphviz.Source(dot_data)
    graph.format = "png"
    graph.render(f"results/tree/{output_file}_full")

    # save full decision tree as png horizontal
    dot_data = tree.export_graphviz(
        classifier,
        out_file=None,
        feature_names=features_train.columns,
        filled=True,
        proportion=True,
        rounded=True,
        max_depth=7,
        rotate=False,
    )
    graph = graphviz.Source(dot_data)
    graph.format = "png"
    graph.render(f"results/tree/{output_file}_full_horizontal")


data_original = pd.read_csv("datasets/dataset.csv", index_col=0)
data_balanced = pd.read_csv("datasets/dataset_balanced.csv", index_col=0)

make_tree(data_original, "Original", "tree")
make_tree(data_balanced, "Balanced", "tree_balanced")
