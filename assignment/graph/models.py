from django.db import models
from django.contrib.auth.models import User


class AutoMpgFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mpg_file = models.FileField(upload_to="data_files/", null=True, blank=True)


class AutoMpgData(models.Model):
    data_file = models.ForeignKey(
        AutoMpgFile, on_delete=models.CASCADE, null=True, blank=True)
    mpg = models.FloatField(null=True, blank=True)
    cylinders = models.IntegerField(null=True, blank=True)
    displacement = models.FloatField(null=True, blank=True)
    horsepower = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    acceleration = models.FloatField(null=True, blank=True)
    model_year = models.IntegerField(null=True, blank=True)
    origin = models.IntegerField(null=True, blank=True)
    car_name = models.CharField(max_length=100, null=True, blank=True)
