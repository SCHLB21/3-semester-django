from django.db import models


class Employees(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Имя', max_length=30)
    surname = models.CharField('Фамилия', max_length=30)
    email = models.EmailField('Почта', max_length=254, unique=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class EmployeeSkills(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    skills = models.TextField('Навыки работника')

    def __str__(self):
        return 'Номер работника: '+str(self.employee_id)

    class Meta:
        verbose_name = 'Навыки работника'
        verbose_name_plural = 'Навыки работников'


class EmployeeSalary(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    desired_salary = models.CharField('Желаемая ЗП', max_length=60)

    def __str__(self):
        return 'Номер работника: '+str(self.employee_id)

    class Meta:
        verbose_name = 'Желаемая ЗП работников'
        verbose_name_plural = 'Желаемая ЗП работника'


class EmployeeRating(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    employee_rating = models.IntegerField()

    def __str__(self):
        return 'Номер работника: '+str(self.employee_id)

    class Meta:
        verbose_name = 'Рейтинг работников'
        verbose_name_plural = 'Рейтинг работника'


class Employers(models.Model):
    id = models.AutoField(primary_key=True)
    employer_name = models.CharField('Работодатель', max_length=45)
    email = models.EmailField('Почта', max_length=254, unique=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Работодатели'
        verbose_name_plural = 'Работодатель'


class NumberEmployees(models.Model):
    id = models.AutoField(primary_key=True)
    employer_id = models.ForeignKey(Employers, on_delete=models.CASCADE)
    employer_number = models.CharField('Количество работников', max_length=40)

    def __str__(self):
        return 'Номер работодателя: '+str(self.employer_id)

    class Meta:
        verbose_name = 'Количество работников'
        verbose_name_plural = 'Количество работников'


class EmployerRating(models.Model):
    id = models.AutoField(primary_key=True)
    employer_id = models.ForeignKey(Employers, on_delete=models.CASCADE)
    employer_rating = models.IntegerField()

    def __str__(self):
        return 'Номер работодателя: '+str(self.mployer_id)

    class Meta:
        verbose_name = 'Рейтинг работодателя'
        verbose_name_plural = 'Рейтинг работодателей'


class Vacancies(models.Model):
    id = models.AutoField(primary_key=True)
    employer_id = models.ForeignKey(Employers, on_delete=models.CASCADE)
    position = models.CharField('Должность', max_length=40)
    description = models.TextField('Описание должности')
    salary = models.CharField('Заработная плата', max_length=60)

    def __str__(self):
        return 'Номер работодателя: '+str(self.mployer_id)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class Resume(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    desired_position = models.CharField('Желаемая должность', max_length=40)

    def __str__(self):
        return 'Номер работодателя: '+str(self.mployer_id)

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    from_id = models.IntegerField()
    to_id = models.IntegerField()
    content = models.TextField('Содержимое сообщения')
