from django.shortcuts import render
import pickle
import numpy as np
# Create your views here.
import os
import environ
from django.conf import settings
from django.shortcuts import render
from django.template import Context
from django.http import JsonResponse

from rest_framework.views import APIView

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated,AllowAny

from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from .serializers import *
env = environ.Env()
environ.Env.read_env()
import boto3

class iris(APIView):

    permission_classes        = [AllowAny]
    serializer_class = iris_serializer

    def post(self, request, format=None):

        a= str(request.data.get('a')).strip()
        b= str(request.data.get('b')).strip()
        c= str(request.data.get('c')).strip()
        d= str(request.data.get('d')).strip()

        s3 = boto3.client('s3')
        s3_bucket = "pickle1234"
        model_name = "iris_model.pkl"
        temp_file_path =  model_name
        
        features=[int(a),int(b),int(c),int(d)]
        np_features=[np.asarray(features)]

        # print(np_features)

        s3.download_file(s3_bucket, model_name, temp_file_path)
        with open(temp_file_path, 'rb') as f:
            model = pickle.load(f)
            
        prediction = model.predict(np_features)
        labels = ['setosa', 'versicolor', 'virginica']

        result = labels[prediction[0]]

        # print(result)

       
        
        dev = {}
        dev["response"]="Data is Shown Below"
        dev["Provided By:"]="RSTIWARI Api Services"
        dev["status"]=200
        dev["data"]=result
        
        return Response(dev)

