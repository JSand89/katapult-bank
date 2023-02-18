from django.db import models
from django.urls import reverse


class Bank(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bank-detail', args=[str(self.id)])

