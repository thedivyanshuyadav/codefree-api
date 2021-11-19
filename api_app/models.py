from django.db import models

# Create your models here.
class IrisModel(models.Model):
    sepal_length = models.FloatField('sepal_length')
    sepal_width = models.FloatField('sepal_width')
    petal_length = models.FloatField('petal_length')
    petal_width = models.FloatField('petal_width')
    iris_class = models.CharField('iris_class',max_length=255)