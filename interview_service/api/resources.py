from import_export import resources
from .models import (Employees, EmployeeSkills, EmployeeSalary, EmployeeRating, Employers, NumberEmployees,
                     EmployerRating, Vacancies, Resume, Message)


class EmployeesResource(resources.ModelResource):
    class Meta:
        model = Employees


class EmployeeSkillsResource(resources.ModelResource):
    class Meta:
        model = EmployeeSkills


class EmployeeSalaryResource(resources.ModelResource):
    class Meta:
        model = EmployeeSalary


class EmployeeRatingResource(resources.ModelResource):
    class Meta:
        model = EmployeeRating


class EmployersResource(resources.ModelResource):
    class Meta:
        model = Employers


class NumberEmployeesResource(resources.ModelResource):
    class Meta:
        model = NumberEmployees


class EmployerRatingResource(resources.ModelResource):
    class Meta:
        model = EmployerRating


class VacanciesResource(resources.ModelResource):
    class Meta:
        model = Vacancies


class ResumeResource(resources.ModelResource):
    class Meta:
        model = Resume


class MessageResource(resources.ModelResource):
    class Meta:
        model = Message
