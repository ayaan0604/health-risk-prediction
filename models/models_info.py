MODEL_FILE_LOCATION={
    'diabetes' : "models/diabetes/decison_tree_diabetes_v2.pkl",
    'cardio_disease' : "models/heart disease/model/logistic_regression_cardio_model_v2.pkl",
    #'liver_disease' : "models/liver/randomForest_fatty_liver.pkl",
    'hypertension'  : "models/hypertension/hypertension_model_logistic_v2.pkl",
    'obesity' : "models/Obesity/Obesity_logisticRegression_v2.pkl",
    'cancer' : "models/Cancer/Cancer_LogisticRegression_v2.pkl"
}

#make sure the input features are in the correct
#order as accepted by the model
#the get_feature_names function comes in handy
MODEL_INPUT_FEATURES={     
    'diabetes' : ['age', 'bmi'],

    'cardio_disease' : ['age', 'smoke', 'alco','active', 'bmi', 'male', 'female'],

    #'liver_disease' : ['age', 'male', 'female', 'bmi', 'smoke'],

    'hypertension' : ['male', 'age', 'bmi', 'smoke', 'female'],

    'obesity' : ['male','female', 'age', 'smoke', 'bmi', 'alco',
                'water_intake', 'caloric_food', 'meals', 'active'],

    'cancer' : ['male', 'female', 'age', 'bmi', 'smoke', 'active',
                'alco']
}

# a very useful function
def get_feature_names(file_address):
    import pickle
    model=pickle.load(open(file_address, 'rb'))
    return model.feature_names_in_
    #print(model.feature_names_in_)

