import pickle

import pandas as pd

# available models: tree, tree_balanced, bayes, ada, mlp
MODEL = "tree_balanced"

match MODEL:
    case "tree_balanced":
        with open("models/tree_balanced.model", "rb") as f:
            loaded_model = pickle.load(f)
    case "tree":
        with open("models/tree.model", "rb") as f:
            loaded_model = pickle.load(f)
    case "bayes":
        with open("models/bayes.model", "rb") as f:
            loaded_model = pickle.load(f)
    case "ada":
        with open("models/ada.model", "rb") as f:
            loaded_model = pickle.load(f)
    case "mlp":
        with open("models/mlp.model", "rb") as f:
            loaded_model = pickle.load(f)
    case _:
        with open("models/tree_balanced.model", "rb") as f:
            loaded_model = pickle.load(f)

# input from user
# logic will be needed to convert binned features
input_data = [
    {
        "HighBP": 0,
        "HighChol": 0,
        "CholCheck": 0,
        "Smoker": 0,
        "Stroke": 1,
        "PhysActivity": 0,
        "Fruits": 0,
        "Veggies": 0,
        "HvyAlcoholConsump": 0,
        "AnyHealthcare": 0,
        "NoDocbcCost": 0,
        "GenHlth": 3,
        "DiffWalk": 0,
        "Sex": 0,
        "Age": 8,
        "Education": 0,
        "Income": 0,
        "BMI_bin": 0,
        "MentHlth_bin": 0,
        "PhysHlth_bin": 0,
        "Diabetes_bin": 0,
    }
]

data = pd.DataFrame(input_data)

result = int(loaded_model.predict(data)[0])
print(result)  # 1 if the model predicts heart disease, otherwise 0
