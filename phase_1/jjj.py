import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 2000

df = pd.DataFrame({
    "montant": rng.integers(100, 5000, n),
    "volume_passees": rng.uniform(1, 50, n).round(2),
    "commission": rng.uniform(0.5, 10, n).round(2),
    "destination_country": rng.choice(["FRANCE", "GERMANY", "SPAIN", "ITALY"], n),
})

# Invented rule so the model has something to learn:
# higher commission and lower volume -> more likely to abandon,
# and Spain gets a small extra push
score = (
    0.6 * (df["commission"] - 5)
    - 0.05 * (df["volume_passees"] - 25)
    + (df["destination_country"] == "SPAIN") * 1.0
)
p = 1 / (1 + np.exp(-score))
df["abandon"] = (rng.random(n) < p).astype(int)

df.to_csv("donnees_scikit.csv", index=False)
print(df.head())
print(df["abandon"].value_counts())