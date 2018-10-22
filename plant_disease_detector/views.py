import datetime
import pickle
import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from api.settings import BASE_DIR

from custom_code import image_converter

@api_view(['GET'])
def __index__function(request):
    start_time = datetime.datetime.now()
    elapsed_time = datetime.datetime.now() - start_time
    elapsed_time_ms = (elapsed_time.days * 86400000) + (elapsed_time.seconds * 1000) + (elapsed_time.microseconds / 1000)
    return_data = {
        "error" : "0",
        "message" : "Successful",
        "restime" : elapsed_time_ms
    }
    return HttpResponse(json.dumps(return_data), content_type='application/json; charset=utf-8')

@api_view(['POST'])
def __predict_plant_disease(request):
    try:
        if request.body:
            request_data = request.data["plant_image"]
            header, image_data = request_data.split(';base64,')
            image_array, err_msg = image_converter.convert_image(image_data)
            if image_array != None :
                model_file = f"{BASE_DIR}/ml_model/random_forest_classifier_99.15.pkl"
                saved_classifier_model = pickle.load(open(model_file,'rb'))
                prediction = saved_classifier_model.predict(image_array) 
                return_data = {
                    "error" : "0",
                    "data" : f"{prediction[0]}"
                }
            else :
                return_data = {
                    "error" : "3",
                    "data" : f"Error : {err_msg}"
                }
        else :
            return_data = {
                "error" : "1",
                "message" : "Request Body is empty",
            }
    except Exception as e:
        return_data = {
            "error" : "3",
            "message" : f"Error : {str(e)}",
        }
    return HttpResponse(json.dumps(return_data), content_type='application/json; charset=utf-8')