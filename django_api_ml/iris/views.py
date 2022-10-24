from django.shortcuts import render

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

env = environ.Env()
environ.Env.read_env()


class iris(APIView):

    permission_classes        = [AllowAny]

    def get(self, request, format=None):

        dev = {}
        dev["response"]="Data is Shown Below"
        dev["Provided By:"]="RSTIWARI Api Services"
        dev["status"]=200
        
        return Response(dev)

