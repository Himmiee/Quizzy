from django.db import models

# Create your models here.

class Course(models.Model):
    list = models.CharField(max_length=200)

    def __str__(self):
         return self.list
    

class Option(models.Model):
    optionID = models.IntegerField( null=True)
    randoms = models.CharField(max_length=200)

    def __str__(self):
         return self.randoms

class Detail(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    question = models.CharField(max_length=200)
    option = models.ManyToManyField(Option)
    answer = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return str(self.question)