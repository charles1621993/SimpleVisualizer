from django.db import models


class Question(models.Model):
   data_text = models.CharField(max_length=2000)
