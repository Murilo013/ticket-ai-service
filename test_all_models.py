import joblib
import numpy as np

type_model = joblib.load("models/type_model.pkl")
priority_model = joblib.load("models/priority_model.pkl")
area_model = joblib.load("models/area_model.pkl")

tests = [
    "Erro ao cadastrar cliente",
    "Sistema muito lento para gerar relatório",
    "Preciso desbloquear meu usuário",
    "Gostaria de uma nova funcionalidade no sistema",
    "Estou sem acesso à internet"
]

print("RESULTADOS:\n")

for text in tests:
    type_pred = type_model.predict([text])[0]
    priority_pred = priority_model.predict([text])[0]
    area_pred = area_model.predict([text])[0]

    print(f"Texto: {text}")
    print(f"  Tipo     : {type_pred}")
    print(f"  Prioridade: {priority_pred}")
    print(f"  Área     : {area_pred}")
    print("-" * 40)