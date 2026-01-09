from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class login_info(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=16)
    

class Reviews(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True,related_name='reviews')
    rating = models.IntegerField()
    comments= models.CharField(max_length=1500)
    publish_time = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return f"{self.user.username} - {self.rating}"
    
