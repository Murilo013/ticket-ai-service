import pandas as pd
import joblib
import os
import sys

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Qual coluna será treinada (type, priority, area)
target = sys.argv[1]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "tickets.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", f"{target}_model.pkl")

data = pd.read_csv(DATA_PATH)

print(data[target].value_counts())

X = data["text"]
y = data[target]

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=1000))
])

pipeline.fit(X, y)

joblib.dump(pipeline, MODEL_PATH)

print(f"Modelo '{target}' treinado com sucesso!")
