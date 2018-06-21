from django.db import models
# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)