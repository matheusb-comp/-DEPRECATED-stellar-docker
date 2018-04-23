from django.db import models

# Create your models here.

class CoreModel(models.Model):
    
    class Meta:
        abstract = True
        managed = False

class Account(CoreModel):
    address = models.CharField(max_length = 56, primary_key = True)
    
    class Meta(CoreModel.Meta):
        db_table = 'accounts'

