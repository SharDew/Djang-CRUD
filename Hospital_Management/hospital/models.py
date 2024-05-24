from django.db import models

# Create your models here.
class Doctors(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 100)
    speciality = models.CharField(max_length = 100)
    fees = models.BigIntegerField()

    
    def __str__(self) -> str:
         return f"{self.name}"

class Patient(models.Model):
    id = models.IntegerField(primary_key=True)
    pname= models.CharField(max_length = 100)
    mobile = models.BigIntegerField()
    address = models.TextField()
    issue = models.CharField(max_length = 200)
    emergency_visit = models.BooleanField()
   
    def __str__(self) -> str:
         return f"{self.pname}"

    

class Ward(models.Model):
     id = models.IntegerField(primary_key=True)
     ward = models.IntegerField()
     name = models.CharField(max_length = 100)
     capacity = models.IntegerField()
    
     


     def __str__(self) -> str:
         return f"{self.name}"


class Patient_History(models.Model):
    pid = models.AutoField(primary_key=True)
    pname= models.ForeignKey(Patient,on_delete=models.CASCADE)
    hname = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctors,on_delete=models.CASCADE)
    pimage = models.ImageField(upload_to="images") 
    file = models.FileField(upload_to="files")


    def __str__(self) -> str:
         return f"{self.pname}"
