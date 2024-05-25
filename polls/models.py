from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    credit=models.IntegerField(default=0)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Poll(models.Model):

    title = models.CharField(max_length=200)
    image=models.ImageField(upload_to='polls/',null=True,blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user} answered {self.question}'