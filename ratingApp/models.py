from django.db import models
from django.contrib.auth.models import User



    

class Reviews(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True,related_name='reviews')
    movie_ids = models.CharField(max_length=50)
    rating = models.IntegerField(null=True)
    comments= models.CharField(max_length=1500)
    publish_time = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return f"{self.user.username} - {self.rating}"
    
