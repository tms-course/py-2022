from django.db import models
from django.utils.translation import gettext_lazy as _


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(_('date published'))
    img = models.ImageField(upload_to="questions/images/", blank=True)


class Choice(models.Model):
    question = models.ForeignKey(Question, 
                                 on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
