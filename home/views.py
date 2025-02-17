from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Student
# Create your views here.

@api_view(['GET','POST','PATCH','PUT','DELETE'])
def index(request):
    print(request.method)
    students = ["Deepak" , "Rahul" , "Hemlata" , "Girish"]
    data = {
        "status" : True,
        "message" : "This is from django rest framework",
        "students" : students,
        "method" : f"Yor are getting this data from {request.method}"

    }
    return Response(data)


@api_view(['POST'])
def create_record(request):
    data = request.data
    Student.objects.create(**data)
    return Response ({
        "status" : True,
        "message" : "record created",
    })

@api_view(['GET'])
def get_record(request):
    students = [
        {
            "id": student.id,
            "name": student.name,
            "dob": student.dob,
            "email": student.email,
            "phone": student.phone,
        }
        for student in Student.objects.all()
    ]
    return Response ({
        "status" : True,
        "message" : "record created",
        "data" : students
    })
