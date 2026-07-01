import pickle
import pandas as pd

from models.models_info import *

from typing import List, Dict


class Model:
    def __init__(self,data):
        self.name = data['name']
        self.modelPath=data['file_location']

        with open(self.modelPath, "rb") as f:
            self.model=pickle.load(f)
        
        self.takesParameters=data['input_features']

        self.info = data["details"]

    #function to get a dataframe of required input features
    def get_dataframe(self, input_features:dict):
        model_req=self.model.feature_names_in_
        req_para={}
        
        
        for i, parameter in enumerate(self.takesParameters):
            # if parameter not in model_req:
            #     raise ValueError(f"Missing feature: {parameter} for model: {self.name} ")
            
            req_para[model_req[i]]=input_features[parameter]
            
        
        return pd.DataFrame([req_para])

    def get_prediction(self, input_features:dict):
        try:
            input_dataframe=self.get_dataframe(input_features)

            predictions=self.model.predict_proba(input_dataframe)
            
            return float(predictions[0][1])
        
        except Exception as e:
            raise ValueError(f"Failed prediction for model: {self.name}", {str(e)})


class Models_Manager():

    def __init__(self):

        self.info_manager = Info_Manager()

        all_models_data :List[Dict] = self.info_manager.get_all_models_info()

        all_models=[]
        for data in all_models_data:
            all_models.append(Model(data))
        
        self.models_list : List[Model] = all_models

        

    def get_all_model_predictions(self,input_data):
    
        results={}

        for m in self.models_list:
            results[m.name]=m.get_prediction(input_data)
        
        #return in json format
        #return json.dumps(results)
        return results
    
    def get_all_models_info(self) -> Dict[str, str] :
        #returns all models info, feature info and 
        # minimum required input features

        final_result = {}

        
        #getting details and features
        info = []
        required_features = set()
        for model in self.models_list:
            data = {}

            data["name"] = model.name
            data["details"] = model.info
            data["input_features"] = model.takesParameters

            for feature in model.takesParameters:
                required_features.add(feature)

            info.append(data)
        
        final_result["models"] = info
        final_result["required_parameters"] = list(required_features)

        final_result["feature_info"] = self.info_manager.get_all_features_info()

        return final_result
    
    ### MORE OPTIONS RELATED TO GETTING MODELS TO BE ADDED


   



#sample input features
inpf={
    'age': 21,
    'smoke': 0,
    'active': 0,
    'alco': 0,
    "male":1,
    "female" : 0,
    'water_intake' : 3,
    'caloric_food' : 1,
    'meals' : 4,
    'bmi':27.0
}



if __name__=='__main__':
    manager = Models_Manager()
    #print(manager.get_all_model_predictions(inpf)) 
    print("\n\n", manager.get_all_models_info())
    