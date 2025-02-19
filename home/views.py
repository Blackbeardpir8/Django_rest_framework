from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Student
from home.serializers import StudentSerializer
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
    student_id = request.GET.get('id')  
    
    if student_id:  
        try:
            student = Student.objects.get(id=student_id) 
            serializer = StudentSerializer(student)
            return Response({
                "status": True,
                "message": "Record fetched",
                "data": serializer.data
            })
        except Student.DoesNotExist:
            return Response({
                "status": False,
                "message": "No record found for the given ID",
                "data": {}
            }, status=404)

    queryset = Student.objects.all()
    serializer = StudentSerializer(queryset, many=True)
    return Response({
        "status": True,
        "message": "All records fetched",
        "data": serializer.data
    })

@api_view(['DELETE'])
def delete_record(request,id):
    
    try:
        student = Student.objects.get(id = id).delete()
        return Response({
            "status" : True,
            "message" : "record deleted",
            "data" : {}
        })
    except Exception as e:
        return Response({
            "status" : False,
            "message" : "invalid id",
            "data" : {}
        })
