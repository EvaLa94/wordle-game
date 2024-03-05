from django.db import models

# Create your models here.


class FiveCharWord(models.Model):
    word = models.CharField(max_length=5)

    def __str__(self):
        return self.word
