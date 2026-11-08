import pandas as pd
from sklearn.datasets import make_classification
import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import GradientBoostingClassifier
import joblib
from sklearn.compose import ColumnTransformer

df = pd.read_csv("donnees_scikit.csv", sep=None, engine="python")
print(df.columns.tolist())

X = df[["montant", "volume_passees", "commission", "destination_country"]]

Y = df["abandon"]

model = Pipeline([
    ("prep", ColumnTransformer([
        ("nums", StandardScaler(), ["montant", "volume_passees", "commission"]),
        ("country", OneHotEncoder(handle_unknown="ignore"), ["destination_country"]),
    ])),
    ('cerveau_logique', GradientBoostingClassifier()),
])

model.fit(X, Y)
joblib.dump(model, "model.joblib")
