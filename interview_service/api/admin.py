from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
from .models import (Employees, EmployeeSkills, EmployeeSalary, EmployeeRating, Employers, NumberEmployees,
                     EmployerRating, Vacancies, Resume, Message)
from .resources import (EmployeesResource, EmployeeSkillsResource, EmployeeSalaryResource, EmployeeRatingResource, EmployersResource, NumberEmployeesResource,
                        EmployerRatingResource, VacanciesResource, ResumeResource, MessageResource)


def change_status(modeladmin, request, queryset):
    queryset.update(status='r')


change_status.short_description = "Пометить как прочитанное"


@admin.register(Employees)
class EmployeesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id", "name", "surname", "email"]
    list_filter = ["id", "name", "surname", "email"]
    search_fields = ["name"]
    resource_class = EmployeesResource

    def get_import_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.CSV,
        )
        return [f for f in formats if f().can_import()]

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.CSV,
        )
        return [f for f in formats if f().can_export()]


@admin.register(EmployeeSkills)
class EmployeeSkillsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id", "employee_id", "skills"]
    list_filter = ["id", "employee_id", "skills"]
    search_fields = ["skills"]
    resource_class = EmployeeSkillsResource

    def get_import_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.CSV,
        )
        return [f for f in formats if f().can_import()]

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.CSV,
        )
        return [f for f in formats if f().can_export()]


@admin.register(EmployeeSalary)
class EmployeeSalaryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id", "employee_id", "desired_salary"]
    list_filter = ["id", "employee_id", "desired_salary"]
    search_fields = ["desired_salary"]
    resource_class = EmployeeSalaryResource

    def get_import_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.CSV,
        )
        return [f for f in formats if f().can_import()]

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.CSV,
        )
        return [f for f in formats if f().can_export()]


@admin.register(EmployeeRating)
class EmployeeRatingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id", "employee_id", "employee_rating"]
    list_filter = ["id", "employee_id", "employee_rating"]
    search_fields = ["employee_rating"]
    resource_class = EmployeeRatingResource

    def get_import_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.CSV,
        )
        return [f for f in formats if f().can_import()]

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.CSV,
        )
        return [f for f in formats if f().can_export()]


@admin.register(Employers)
class EmployersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id", "employer_name", "email"]
    list_filter = ["id", "employer_name", "email"]
    search_fields = ["employer_name"]
    resource_class = EmployersResource

    def get_import_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.CSV,
        )
        return [f for f in formats if f().can_import()]

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.CSV,
        )
        return [f for f in formats if f().can_export()]


@admin.register(NumberEmployees)
class NumberEmployeesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id", "employer_id", "employer_number"]
    list_filter = ["id", "employer_id", "employer_number"]
    search_fields = ["employer_number"]
    resource_class = NumberEmployeesResource

    def get_import_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.CSV,
        )
        return [f for f in formats if f().can_import()]

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.CSV,
        )
        return [f for f in formats if f().can_export()]


@admin.register(EmployerRating)
class EmployerRatingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id", "employer_id", "employer_rating"]
    list_filter = ["id", "employer_id", "employer_rating"]
    search_fields = ["employer_rating"]
    resource_class = EmployerRatingResource

    def get_import_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.CSV,
        )
        return [f for f in formats if f().can_import()]

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.CSV,
        )
        return [f for f in formats if f().can_export()]


@admin.register(Vacancies)
class VacanciesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id", "employer_id", "position", "description", "salary"]
    list_filter = ["id", "employer_id", "position", "description", "salary"]
    search_fields = ["position"]
    resource_class = VacanciesResource

    def get_import_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.CSV,
        )
        return [f for f in formats if f().can_import()]

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.CSV,
        )
        return [f for f in formats if f().can_export()]


@admin.register(Resume)
class ResumeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id", "employee_id", "desired_position",
                    "desired_salary", "skills"]
    list_filter = ["id", "employee_id", "desired_position",
                   "desired_salary", "skills"]
    search_fields = ["desired_position"]
    resource_class = ResumeResource

    def get_import_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.CSV,
        )
        return [f for f in formats if f().can_import()]

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.CSV,
        )
        return [f for f in formats if f().can_export()]


@admin.register(Message)
class MessageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id", "from_id", "to_id", "content", "status"]
    list_filter = ["id", "from_id", "to_id", "content", "status"]
    search_fields = ["content"]
    actions = [change_status]
    resource_class = MessageResource

    def get_import_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.CSV,
        )
        return [f for f in formats if f().can_import()]

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.CSV,
        )
        return [f for f in formats if f().can_export()]
