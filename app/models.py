from django.db import models
from django.db import connections

#registration schema
class User(models.Model):
    username = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)
    class Meta:
        db_table="user"
#note schema
class Note(models.Model):
    username = models.CharField(max_length=255)
    note = models.CharField(max_length=255)
    class Meta:
        db_table="sites"
