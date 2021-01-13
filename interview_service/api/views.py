from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (Employees, Employers)
from .serializers import (EmployeesSerializer, EmployersSerializer)


def index(request):
    return HttpResponse("<h1>Кто я?</h1>")


class EmployeesView(APIView):
    def get(self, request):
        EmployeesApi = Employees.objects.all()
        serializer = EmployeesSerializer(EmployeesApi, many=True)
        return Response({"Employees": serializer.data})


class EmployersView(APIView):
    def get(self, request):
        EmployersApi = Employers.objects.all()
        serializer = EmployersSerializer(EmployersApi, many=True)
        return Response({"Employees": serializer.data})
