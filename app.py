from fastapi import FastAPI, HTTPException
from models_manager import Models_Manager
from requests_manager import Prediction_Request



model_manager = Models_Manager()

app = FastAPI()


# @app.get("/get_results")
# def get_response(request : Request):
#     info=dict(request.query_params)
#     response= model_manager.get_all_model_predictions(info)
#     return response

@app.get("/get_info")
def get_all_models_information():
    return model_manager.get_all_models_info()

@app.post("/results")
async def get_all_models_prediction(request : Prediction_Request):
    try:
        return model_manager.get_all_model_predictions(request.to_input_features())

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))