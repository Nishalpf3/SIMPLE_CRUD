from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="student Name")
    email = models.EmailField(max_length=250, verbose_name="student Email")
    place = models.CharField(max_length=100, verbose_name="student Place")
    cls = models.IntegerField(verbose_name="student class")

    def __str__(self):
        return str(self.id)
