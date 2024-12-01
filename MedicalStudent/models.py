from django.db import models

# Create your models here.
class Student(models.Model):
    StudentRegNumber=models.IntegerField(unique=True)
    StudentName=models.CharField(max_length=50)
    NameOftheProgramme=models.CharField(max_length=100)
    StudentAddress=models.TextField()
    ContactMobileNumber=models.CharField(max_length=10)
    StatusOftheSemesterFee=models.BooleanField(default=False)
    def __str__(self):
        return str(self.StudentRegNumber)

