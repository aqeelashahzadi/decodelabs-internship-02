from django.db import models

 # CharField, TextField, IntegerField, FloatField, DecimalField, BooleanField, EmailField, DateTimeField, DateField, FileField, ImageField, URLField, ForeignKey, OneToOneField, ManyToManyField.
# Create your models here.

class Student(models.Model):  # 'models.Model' se inherit karna hai
    name = models.CharField(max_length=100)
    uni = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    semester = models.IntegerField()    
    image = models.ImageField(upload_to='project_images/', blank=True)

    def __str__(self):
        return self.uni
    
class teachers(models.Model):  # 'models.Model' se inherit karna hai
    name = models.CharField(max_length=100)
    uni = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)

  