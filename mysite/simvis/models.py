from django.db import models


class dataInput(models.Model):
   data_text = models.CharField(max_length=2000)
   def __str__(self):
        return self.data_text
