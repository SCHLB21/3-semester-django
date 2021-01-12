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
