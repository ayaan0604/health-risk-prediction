MODEL_FILE_LOCATION={
    'diabetes' : "models/diabetes/decison_tree_diabetes_v2.pkl",
    'cardio_disease' : "models/heart disease/model/logistic_regression_cardio_model_v2.pkl",
    'liver_disease' : "models/liver/randomForest_fatty_liver.pkl",
    'hypertension'  : "models/hypertension/hypertension_model_logistic_v2.pkl"
}


MODEL_INPUT_FEATURES={
    'diabetes' : ['age', 'bmi'],
    'cardio_disease' : ['age', 'smoke', 'alco','active', 'bmi', 'male', 'female'],
    'liver_disease' : ['age', 'male', 'female', 'bmi', 'smoke'],
    'hypertension' : ['male', 'age', 'bmi', 'smoke', 'female']
}

def get_feature_names(file_address):
    import pickle
    model=pickle.load(open(file_address, 'rb'))
    print(model.feature_names_in_)