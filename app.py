from flask import Flask, render_template, request, jsonify
from models.get_predictions import *


app = Flask(__name__)


@app.route("/get_response", methods=["GET"])
def get_results():
    if request.method=='GET':
        info=request.args.to_dict()
        response=get_all_model_predictions(models_list,info)
        return response

if __name__=="__main__":
    app.run()


