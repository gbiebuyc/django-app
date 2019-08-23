from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Company(models.Model):
    name = models.CharField(max_length=200)
    logo = models.URLField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    class Meta:
        verbose_name_plural = 'All companies'
    def __str__(self):
        return self.name

class SupplierCompany(Company):
    class Meta:
        verbose_name_plural = 'Supplier companies'

class ClientCompany(Company):
    taxonomy_package = models.URLField(max_length=200, blank=True)
    class Meta:
        verbose_name_plural = 'Client companies'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ManyToManyField('company')

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
