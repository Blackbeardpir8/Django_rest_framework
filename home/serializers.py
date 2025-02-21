from rest_framework import serializers
from home.models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Student
        fields = '__all__'

class BookSerializer(serializers.Serializer):
    book_title = serializers.CharField(max_length=100)
    authoer = serializers.CharField(max_length=100)
    price = serializers.FloatField( )