from django.db import models
# from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Auth(models.Model):
    auther= models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    title=models.CharField(max_length=64)
    age=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)