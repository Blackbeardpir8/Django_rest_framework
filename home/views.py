from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view()
def index(request):
    data = {
        "status" : True,
        "message" : "This is from django rest framework"
    }
    return Response(data)