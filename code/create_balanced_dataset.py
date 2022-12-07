import pandas as pd

data_original = pd.read_csv("datasets/dataset.csv", index_col=0)

print(
    f'original pos occurences: {len(data_original[data_original["HeartDiseaseorAttack"] == 1])}'
)
print(
    f'original neg occurences: {len(data_original[data_original["HeartDiseaseorAttack"] == 0])}'
)


pos_sample = data_original[data_original["HeartDiseaseorAttack"] == 1]
neg_sample = data_original[data_original["HeartDiseaseorAttack"] == 0].sample(
    n=len(pos_sample)
)
data_balanced = pd.concat([pos_sample, neg_sample], ignore_index=True)
data_balanced = data_balanced.sample(frac=1)

print(
    f'balanced pos occurences: {len(data_balanced[data_balanced["HeartDiseaseorAttack"] == 1])}'
)
print(
    f'balanced neg occurences: {len(data_balanced[data_balanced["HeartDiseaseorAttack"] == 0])}'
)

data_balanced.to_csv("datasets/dataset_balanced.csv")
