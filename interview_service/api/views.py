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

    def post(self, request):
        EmployeesApi = request.data.get('Employees')
        serializer = EmployeesSerializer(data=EmployeesApi)
        if serializer.is_valid(raise_exception=True):
            employee_saved = serializer.save()
        return Response({"success": "Employee '{}' created successfully".format(employee_saved.name)})


class EmployersView(APIView):
    def get(self, request):
        EmployersApi = Employers.objects.all()
        serializer = EmployersSerializer(EmployersApi, many=True)
        return Response({"Employers": serializer.data})

    def post(self, request):
        EmployersApi = request.data.get('Employers')
        serializer = EmployersSerializer(data=EmployersApi)
        if serializer.is_valid(raise_exception=True):
            employer_saved = serializer.save()
        return Response({"success": "Employer '{}' created successfully".format(employer_saved.employer_name)})
# POST запрос для Employees
# {
#     "Employees":{
#         "id": 6,
#         "name": "Dima",
#         "surname": "Komkov",
#         "email": "komkovdddf@mail.ru"
#     }
# }

# POST запрос для Employers
# {
#     "Employers":{
#         "id": 3,
#         "employer_name": "Apple",
#         "email": "ktoonktoon@mail.ru"
#     }
# }
