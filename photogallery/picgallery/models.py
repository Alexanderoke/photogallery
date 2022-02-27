from django.db import models

# Create your models here.
'''
Model class for picture categories
'''

class Category(models.Model):
  name = models.CharField(max_length=100, null=False, blank=False)

  def __str__(self):
    return self.name


'''
Model class for picture categories
'''

class Category(models.Model):
  name = models.CharField(max_length=100, null=False, blank=False)

  def __str__(self):
    return self.name
