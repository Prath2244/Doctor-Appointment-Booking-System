from django.db import models

class Userinfo(models.Model):
    email=models.CharField(max_length=100)
    pssword=models.CharField(max_length=100)

    def __str__(self):
        return self.email
    
class Doctorinfo(models.Model):
    doc_name=models.CharField(max_length=100)
    doc_img=models.ImageField(upload_to='doctors/')
    spec=models.CharField(max_length=100)

    def __str__(self):
        return self.doc_name


class Register(models.Model):
    d_name=models.CharField(max_length=100)
    p_name=models.CharField(max_length=60)
    name=models.CharField(max_length=100)
    reason=models.CharField(max_length=100)

    def __str__(self):
        return self.p_name



# Create your models here.
