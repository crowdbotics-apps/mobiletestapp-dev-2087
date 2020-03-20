from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class SomeModel(models.Model):
    "Generated Model"
    test123 = models.BigIntegerField()


class Test(models.Model):
    "Generated Model"
    testField = models.DecimalField(max_digits=30, decimal_places=10,)
    testField2 = models.CharField(max_length=256,)


class Asdsds(models.Model):
    "Generated Model"
    asdsa = models.BigIntegerField()


class SS(models.Model):
    "Generated Model"
    asA = models.BigIntegerField()
