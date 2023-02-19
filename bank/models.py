import re

from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator, MaxLengthValidator

def validate_string(value):
    if not isinstance(value, str):
        raise ValidationError("This field only accepts string values.")

class Bank(models.Model):
    name = models.CharField(max_length=50,
    validators=[MaxLengthValidator(limit_value=50,message="El nombre debe tener menos de 50 caracteres")])

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bank-detail', args=[str(self.id)])


class Supplier(models.Model):   
    name = models.CharField(max_length=50,validators=[validate_string])
    nit = models.CharField(max_length=50,validators=[RegexValidator(r'^\d{9}-\d$')])
    contact_person_name = models.CharField(max_length=50)
    contact_person_phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('supplier-detail', args=[str(self.id)])


class BankAccount(models.Model):
    name = models.ForeignKey(Bank,on_delete=models.CASCADE)
    account_number = models.CharField(max_length=15, blank=True)
    nit = models.ForeignKey(Supplier,on_delete=models.CASCADE)

    def __str__(self):
        return self.account_number
