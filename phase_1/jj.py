import pandas as pd
from sklearn.datasets import make_classification

# 1. Générer un jeu de données synthétique (1000 lignes, 4 colonnes de caractéristiques)
# n_samples détermine le nombre de lignes (1000)
X, y = make_classification(
    n_samples=1000, n_features=4, n_classes=2, random_state=42
)

# 2. Créer un DataFrame Pandas pour structurer les données
df = pd.DataFrame(X, columns=[f"caracteristique_{i+1}" for i in range(4)])

# Ajouter la colonne cible (target) contenant les classes à prédire
df["cible"] = y

# 3. Exporter le DataFrame en fichier CSV
# index=False permet d'éviter d'ajouter une colonne de numérotation inutile
df.to_csv("donnees_scikit.csv", index=False)

print(
    f"Le fichier CSV a été généré avec succès ! Dimensions : {df.shape[0]} lignes et {df.shape[1]} colonnes."
)
