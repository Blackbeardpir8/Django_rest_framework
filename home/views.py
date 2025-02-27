from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Student,Book,Product
from home.serializers import StudentSerializer,BookSerializer,ProductSerializer
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework import generics
# Create your views here.

class StudentModelListView(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self, request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class StudentAPI(APIView):
    def get(self, request):
        return Response({
            "status" : True,
            "message" : "This is a get API"
    })

    def post(self, request):
        return Response({
            "status" : True,
            "message" : "This is a post API"
    })

    def patch(self, request):
        return Response({
            "status" : True,
            "message" : "This is a aptch API"
    })

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
    serializer = StudentSerializer(data = data)
    if not serializer.is_valid():
        return Response ({
            "status" : False,
            "message" : "record not created",
            "errors" : serializer.errors
        })
    serializer.save()
    return Response({
        "status" : True,
        "message" : "record created",
        "data" : serializer.data
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


@api_view(['PATCH'])
def update_record(request):
    data = request.data
    if data.get('id') is None:
        return Response({
            "status" : False,
            "message" : "record not created",
            "errors" : "id is required"
        })

    student_obj = Student.objects.get(id = data.get('id'))
    serializer = StudentSerializer(student_obj,data = data, partial = True)
    if not serializer.is_valid():
        return Response ({
            "status" : False,
            "message" : "record not updated",
            "errors" : serializer.errors
        })
    serializer.save()
    return Response({
        "status" : True,
        "message" : "record updated",
        "data" : serializer.data
    })

# Book Serializerand views
@api_view(['POST'])
def create_book(request):
    data = request.data
    serializer = BookSerializer(data = data)
    if not serializer.is_valid():
        return Response ({
            "status" : False,
            "message" : "record not created",
            "errors" : serializer.errors
        })
    print(serializer.validated_data)
    return Response({
        "status": True,
        "message": "Book created successfully",
        "data": serializer.data
    }, status=201)
    
@api_view(['POST'])
def create_record(request):
    serializer = BookSerializer(data=request.data)

    if not serializer.is_valid():
        print(serializer.errors)  # Debugging step
        return Response({
            "status": False,
            "message": "Validation failed",
            "errors": serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)
    
    book = serializer.save()  # Ensure this is being called
    return Response({
        "status": True,
        "message": "Record created successfully",
        "data": serializer.data,
    }, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def get_books(request):
    queryset = Book.objects.all()
    serialier = BookSerializer(queryset, many = True)
    return Response({
        "status" : True,
        "message" : "record fetched",
        "data" : serialier.data
    })


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
