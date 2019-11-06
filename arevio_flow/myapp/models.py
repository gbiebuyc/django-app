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

class Taxonomy(models.Model):
    name = models.CharField(max_length=200)
    # xbrl_template = 
    arelleCmdLine_options = models.TextField()
    class Meta:
        verbose_name_plural = 'Taxonomies'
    def __str__(self):
        return self.name

class AnnualReport(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    taxonomy = models.ForeignKey(Taxonomy, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # updated_by = models.ForeignKey(User, on_delete=models.CASCADE)
