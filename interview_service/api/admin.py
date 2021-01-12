from django.contrib import admin
from .models import Employees
from .models import EmployeeSkills
from .models import EmployeeSalary
from .models import EmployeeRating
from .models import Employers
from .models import NumberEmployees
from .models import EmployerRating
from .models import Vacancies
from .models import Resume
from .models import Message


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "surname", "email")


@admin.register(EmployeeSkills)
class EmployeeSkillsAdmin(admin.ModelAdmin):
    list_display = ("id", "employee_id", "skills")


@admin.register(EmployeeSalary)
class EmployeeSalaryAdmin(admin.ModelAdmin):
    list_display = ("id", "employee_id", "desired_salary")


@admin.register(EmployeeRating)
class EmployeeRatingAdmin(admin.ModelAdmin):
    list_display = ("id", "employee_id", "employee_rating")


@admin.register(Employers)
class EmployersAdmin(admin.ModelAdmin):
    list_display = ("id", "employer_name", "email")


@admin.register(NumberEmployees)
class NumberEmployeesAdmin(admin.ModelAdmin):
    list_display = ("id", "employer_id", "employer_number")


@admin.register(EmployerRating)
class EmployerRatingAdmin(admin.ModelAdmin):
    list_display = ("id", "employer_id", "employer_rating")


@admin.register(Vacancies)
class VacanciesAdmin(admin.ModelAdmin):
    list_display = ("id", "employer_id", "position", "description", "salary")


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("id", "employee_id", "desired_position")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "from_id", "to_id", "content")
