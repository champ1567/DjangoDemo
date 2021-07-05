from django.db import models

# Create your models here.
class Informations(models.Model):
    citizenid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    vehicle = models.CharField(max_length=255)
    bf_date = models.CharField(max_length=255)
    bf_time = models.CharField(max_length=255)
    bf_parish = models.CharField(max_length=255)
    bf_district = models.CharField(max_length=255)
    bf_province = models.CharField(max_length=255)
    bf_country = models.CharField(max_length=255)
    at_parish = models.CharField(max_length=255)
    at_district = models.CharField(max_length=255)
    at_province = models.CharField(max_length=255)


    def __str__(self):
        return self.citizenid