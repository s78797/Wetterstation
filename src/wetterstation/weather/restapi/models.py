from django.db import models

"""
This file contains all models for the wetterstation application.
Each model represents a single table in our database.
"""


# Create your models here.


class MeasurementSession(models.Model):
    session_id = models.IntegerField(unique=True, primary_key=True)
    data_volume = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)


class Temperature(models.Model):
    degrees = models.DecimalField(max_digits=5, decimal_places=1)
    time = models.DateTimeField()
    measurement_session = models.OneToOneField(MeasurementSession, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'created: ' + str(self.time) + ', temperature: ' + str(self.degrees)


class Wind(models.Model):
    speed = models.DecimalField(max_digits=5, decimal_places=1)  # in m/s
    direction = models.DecimalField(max_digits=5, decimal_places=1)  # in degrees
    time = models.DateTimeField()
    measurement_session = models.OneToOneField(MeasurementSession, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'created: ' + str(self.time) + ', speed: ' + str(self.speed) + ', direction: ' + str(self.direction)


class Image(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m')
    time = models.DateTimeField()
    measurement_session = models.OneToOneField(MeasurementSession, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.image.name

# class Configurations(models.Model):
#     maintenance_mode = models.CharField(max_length=20)
#     res_hight = models.IntegerField
#     res_width = models.IntegerField
#
#     def __str__(self):
#         return 'maintenance: ' + self.maintenance_mode + 'resolution: ' + self.res_hight + 'x' + self.res_width
#
#
# class ConfigSession(models.Model):
#     configuration = models.OneToOneField(Configurations, primary_key=True)
#     start_time = models.TimeField(auto_now_add=True)
#     applied = models.BooleanField
#     # TODO add refrence to user here
