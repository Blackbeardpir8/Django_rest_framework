from rest_framework import serializers
from home.models import Student,Book

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