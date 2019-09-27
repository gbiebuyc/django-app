from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(blank=True, verbose_name="Logo image file")
    address = models.CharField(max_length=200, blank=True)
    CLIENT = 1
    SUPPLIER = 2
    COMPANY_TYPE_CHOICES = [
        (CLIENT, 'Client'),
        (SUPPLIER, 'Supplier'),
    ]
    company_type = models.IntegerField(
        choices=COMPANY_TYPE_CHOICES,
        default=CLIENT,
    )
    users = models.ManyToManyField(User, blank=True)
    class Meta:
        verbose_name_plural = 'Companies'
    def __str__(self):
        return self.name


class AnnualRapport(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    taxonomy = models.FileField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
