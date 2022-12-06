import pandas as pd

data_original = pd.read_csv("datasets/dataset.csv", index_col=0)

pos_sample = data_original[data_original["HeartDiseaseorAttack"] == 1]
neg_sample = data_original[data_original["HeartDiseaseorAttack"] == 0]
ratio = len(neg_sample) // len(pos_sample)

print(f"Original neg/pos ratio: {ratio}")
print(f"pos size: {len(pos_sample)}\nneg size: {len(neg_sample)}\n")

data_balanced = data_original.copy()
for _ in range(ratio):
    data_balanced = pd.concat([data_balanced, pos_sample], ignore_index=True)
data_balanced = data_balanced.sample(frac=1)

b_pos_sample = data_balanced[data_balanced["HeartDiseaseorAttack"] == 1]
b_neg_sample = data_balanced[data_balanced["HeartDiseaseorAttack"] == 0]

print("After balancing:")
print(f"pos size: {len(b_pos_sample)}\nneg size: {len(b_neg_sample)}\n")

data_balanced.to_csv("datasets/dataset_balanced.csv")
