from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

class Post(models.Model):
    id = models.AutoField( primary_key=True)
    first_name=models.CharField(max_length=15, verbose_name='Имя')
    last_name=models.CharField(max_length=25,  verbose_name='Фамилия')
    address=models.CharField(max_length=200, verbose_name='Адрес')
    lat=models.DecimalField(max_digits=10, decimal_places=8, blank=False, null=False, verbose_name='Широта')
    lot=models.DecimalField(max_digits=11, decimal_places=8, blank=False, null=False, verbose_name='Долгота')
    phone_number = PhoneNumberField()
     	
    def __str__(self):
        return self.first_name