from rest_framework import serializers


class EmployeesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=30)
    surname = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=254)


class EmployersSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    employer_name = serializers.CharField(max_length=45)
    email = serializers.EmailField(max_length=254)
