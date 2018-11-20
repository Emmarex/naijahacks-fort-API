from django.urls import path
from . import views

urlpatterns = [
    path('',views.__index__function),
    path('predict',views.predict_plant_disease)
]