from django.db import models


class Appdata(models.Model):
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    position_z = models.IntegerField()
    magnetic_x = models.IntegerField()
    magnetic_y = models.IntegerField()
    magnetic_z = models.IntegerField()
    rotation_x = models.IntegerField()
    rotation_y = models.IntegerField()
    rotation_z = models.IntegerField()
    acc_x = models.IntegerField()
    acc_y = models.IntegerField()
    acc_z = models.IntegerField()
    tracking_lost = models.BooleanField()
    user_id = models.IntegerField()


class Localization(models.Model):
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    localization_x = models.IntegerField()
    localization_y = models.IntegerField()
