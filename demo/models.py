from django.db import models

# Create your models here.
class Email(models.Model):
    email=models.EmailField(max_length=254,blank=True,null=True)
    mobile=models.TextField()
    def __str__(self):
        return str(self.email)

# class Moblie(models.Model):
#     email_id=models.ForeignKey(Email,on_delete=models.CASCADE,null=True)
#     moblie=models.TextField()