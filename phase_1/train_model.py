
from sklearn.pipeline import Pipeline
from sklearn.preprocession import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

pipeline_data = Pipeline([
    ('nettoyeur', StandardScaler()),
    ('cerveau_logique', LogisticRegression())
])

pipeline_data.fit(X_train, Y_train)

joblib.dump(pipeline_data, 'trained_model.joblib')