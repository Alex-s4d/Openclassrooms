import joblib
import re
#Api import
from fastapi import FastAPI
from ScoringCredits import ScoringCredit
import pickle
import pandas as pd
 
 
# On crée notre instance FastApi puis on définit l'objet enstiment
app = FastAPI()
 

classifier = joblib.load('pipeline_final.pkl')
# Nos différents endpoints
 
@app.get('/')
def index():
    return {'message': 'Welcome to the scoring credit API'}
 
@app.post('/predict')
def predict_scoringcredit(data: ScoringCredit):
    # Convertir les données reçues en DataFrame pandas
    input_data = pd.DataFrame([data.dict()])

    # Utiliser la pipeline pour effectuer des prédictions
    prediction = classifier.predict(input_data)

    # Interprétation de la prédiction
    prediction_label = "Risque de crédit élevé, accord refusé" if prediction == 1 else "Risque de crédit faible, accord accepté"

    return {
        'prediction': prediction_label
    }


#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)