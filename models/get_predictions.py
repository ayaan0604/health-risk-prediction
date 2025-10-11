import pickle
import pandas as pd
from models_info import *

class Model:
    def __init__(self,name, modelPath):
        self.name=name

        with open(modelPath, "rb") as f:
            self.model=pickle.load(f)
        
        self.takesParameters=MODEL_INPUT_FEATURES[name]

    #function to get a dataframe of required input features
    def get_dataframe(self, input_features:dict):
        model_req=self.model.feature_names_in_
        req_para={}
        
        i=0
        for parameter in self.takesParameters:
            req_para[model_req[i]]=input_features[parameter]
            i+=1
        
        return pd.DataFrame([req_para])

    def get_prediction(self, input_features:dict):

        input_dataframe=self.get_dataframe(input_features)

        predictions=self.model.predict_proba(input_dataframe)
        
        return predictions[0][1]
    


inpf={
    'age': 27,
    'bmi':18.5,
    'smoke': 0,
    'alco': 0,
    'active': 1,
    "male":1,
    "female" : 0
}

all_models=[]
for model_name, address in MODEL_FILE_LOCATION.items():
    all_models.append(Model(model_name, address))

for m in all_models:
    print(f"{m.name}: {(m.get_prediction(inpf) * 100):.2f}% \n")
    