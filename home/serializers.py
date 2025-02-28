from rest_framework import serializers
from home.models import Student,Book,Product
from django.contrib.auth.models import User 

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Student
        fields = '__all__'

class BookSerializer(serializers.Serializer):
    book_title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    price = serializers.FloatField()

    def create(self, validated_data):
        book = Book.objects.create(**validated_data)
        return book
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Product
        fields = '__all__'

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 100)
    password = serializers.CharField(max_length = 100)
    first_name = serializers.CharField(max_length = 100)
    last_name = serializers.CharField(max_length = 100)

    def validate(self, attrs):
        if User.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError({'username': 'Username already exists'})
        return attrs
    
    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']

        user = User.objects.create_user(
            username=username,password=password,first_name=first_name,last_name = last_name
        )
    
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 100)
    password = serializers.CharField(max_length = 100)