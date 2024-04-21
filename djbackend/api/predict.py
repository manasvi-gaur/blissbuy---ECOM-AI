import joblib
import os
from sklearn.preprocessing import StandardScaler

ROOT = os.path.dirname(__file__)

def predict(data):
    scaler = StandardScaler()
    # data2 = scaler.fit_transform(data)
    # data_scaled = scaler.transform(data)
    
    model = joblib.load(os.path.join(ROOT,'ecomModel.joblib'))
    pred = model.predict(data)
    return pred