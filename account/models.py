from django.db import models

# Create your models here.
class Registration(models.Model):
    
    name=models.CharField(max_length= 255)
    phone=models.CharField(max_length=255,unique=True)
    course=models.CharField(max_length=255,unique=True)

class SaveOtp(models.Model):
    reg=models.OneToOneField(Registration,on_delete=models.CASCADE)
    otp=models.CharField(max_length=255)
    
    def __str__(self):
        return self.phone_number