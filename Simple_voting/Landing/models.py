from django.db import models
from django.contrib.auth.models import User

# models.CharField
# models.IntegerField
# models.FloatField


class Voting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_gl = models.CharField(max_length=200)
    opis_gl = models.CharField(max_length=2000)
    ans_1 = models.CharField(max_length=100)
    ans_2 = models.CharField(max_length=100)
    question = models.CharField(max_length=1000)
    count_1 = models.IntegerField()
    count_2 = models.IntegerField()
    count_all = models.IntegerField()
    persent_1 = models.FloatField()
    persent_2 = models.FloatField()



# Create your models here.
