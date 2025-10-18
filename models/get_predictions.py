import pickle
import pandas as pd
if __name__ =="__main__":
    from models_info import *
else:
    from .models_info import *
import sklearn

class Model:
    def __init__(self,name):
        self.name=name
        self.modelPath=MODEL_FILE_LOCATION[name]

        with open(self.modelPath, "rb") as f:
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
        
        return float(predictions[0][1])


def get_all_models():
    all_models=[]
    for model_name in MODEL_FILE_LOCATION:
        all_models.append(Model(model_name))
    return all_models

def get_all_model_predictions(all_models,input_data):
    
    results={}

    for m in all_models:
        results[m.name]=m.get_prediction(input_data)
    
    #return in json format
    #return json.dumps(results)
    return results
   



#sample input features
inpf={
    'age': 21,
    'bmi':27.0,
    'smoke': 0,
    'alco': 0,
    'active': 0,
    "male":1,
    "female" : 0,
    'water_intake' : 3,
    'caloric_food' : 1,
    'meals' : 4
}

models_list=get_all_models()

if __name__=='__main__':
    print(get_all_model_predictions(models_list, inpf)) 
    