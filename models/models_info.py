MODEL_FILE_LOCATION={
    'diabetes' : "models/diabetes/decison_tree_diabetes_v2.pkl",
    'cardio_disease' : "models/heart disease/model/logistic_regression_cardio_model_v2.pkl",
    'liver_disease' : "models/liver/randomForest_fatty_liver.pkl",
    'hypertension'  : "models/hypertension/hypertension_model_logistic.pkl"
}


MODEL_INPUT_FEATURES={
    'diabetes' : ['age', 'bmi'],
    'cardio_disease' : ['age', 'smoke', 'alco','active', 'bmi', 'male', 'female'],
    'liver_disease' : ['age', 'male', 'female', 'bmi', 'smoke'],
    'hypertension' : ['male', 'age', 'bmi', 'smoke', 'female']
}


#import pickle
#model=pickle.load(open("models/hypertension/hypertension_model_logistic.pkl", 'rb'))

#print(model.feature_names_in_)