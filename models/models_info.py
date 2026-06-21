import json

class Info_Manager:
    def __init__(self):
        self.file = "models/models_info.json"

    def get_all_models_info(self):
        
        with open(self.file, "r") as f:
            data = json.load(f)['models']

        return data

    def get_all_features_info(self):
        with open(self.file, "r") as f:
            data = json.load(f)["feature_definitions"]
        
        return data




        



# a very useful function
def get_feature_names(file_address):
    import pickle
    model=pickle.load(open(file_address, 'rb'))
    return model.feature_names_in_
    #print(model.feature_names_in_)

