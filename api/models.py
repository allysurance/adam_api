from django.db import models

# Create your models here.

"""
Documentation for this module:
This module of django contains all tables of the databse .
"""
class user(models.Model):
    """user data of the people interacting with the bot """
    sender_id = models.CharField(max_length = 250 , default = 'NULL')
    smoking_status = models.CharField(max_length = 250 , default = 'NULL')
    premium_term = models.CharField(max_length = 250 , default = 'NULL')
    maturity_term = models.CharField(max_length = 250 , default = 'NULL')
    lumpsum = models.CharField(max_length = 250 , default = 'NULL')
    premium_afford = models.CharField(max_length = 250 , default = 'NULL')    

    def __str__(self):
        return self.sender_id