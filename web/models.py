from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)

    def __str__(self):
        return "{} - token".format(str(self.user))


class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)

    # this function return a good name for expense objects in admin site
    def __str__(self):
        return "{} - {}".format(str(self.date), str(self.amount))
        # return "{}-{}".format(self.date, self.amount)



class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)

    def __str__(self):
        return "{} - {}".format(str(self.date), str(self.amount))
