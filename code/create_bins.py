"""
Attributes to bin:

BMI
MentHlth
PhysHlth
Diabetes
"""

import pandas as pd
import numpy as np

data = pd.read_csv("datasets/dataset_unmodified.csv")

# add columns to data frame
data["BMI_bin"] = np.nan
data["MentHlth_bin"] = np.nan
data["PhysHlth_bin"] = np.nan
data["Diabetes_bin"] = np.nan

# fill BMI_bin
data.loc[data["BMI"] < 18.5, "BMI_bin"] = 0
data.loc[(data["BMI"] >= 18.5) & (data["BMI"] < 25), "BMI_bin"] = 1
data.loc[(data["BMI"] >= 25) & (data["BMI"] < 30), "BMI_bin"] = 2
data.loc[data["BMI"] >= 30, "BMI_bin"] = 3

# fill MentHlth_bin
data.loc[data["MentHlth"] <= 10, "MentHlth_bin"] = 0
data.loc[(data["MentHlth"] > 10) & (data["MentHlth"] <= 20), "MentHlth_bin"] = 1
data.loc[data["MentHlth"] > 20, "MentHlth_bin"] = 2

# fill PhysHlth_bin
data.loc[data["PhysHlth"] <= 10, "PhysHlth_bin"] = 0
data.loc[(data["PhysHlth"] > 10) & (data["PhysHlth"] <= 20), "PhysHlth_bin"] = 1
data.loc[data["PhysHlth"] > 20, "PhysHlth_bin"] = 2

# fill Diabetes_bin
data.loc[data["Diabetes"] == 0, "Diabetes_bin"] = 0
data.loc[(data["Diabetes"] == 1) | (data["Diabetes"] == 2), "Diabetes_bin"] = 1

# write new dataset with added attributes
data.to_csv("datasets/dataset_attributes_added.csv")

# write new dataset with old attributes removed
data = data.drop(["BMI", "MentHlth", "PhysHlth", "Diabetes"], axis=1)
data.to_csv("datasets/dataset.csv")
