from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models_manager import Models_Manager
from requests_manager import Prediction_Request
import os

origins = os.getenv("ALLOWED_ORIGINS", "").split(",")




model_manager = Models_Manager()

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)


@app.get("/get_info")
def get_all_models_information():
    return model_manager.get_all_models_info()

@app.post("/results")
async def get_all_models_prediction(request : Prediction_Request):
    try:
        return model_manager.get_all_model_predictions(request.to_input_features())

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))