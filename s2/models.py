from django.db import models

# Create your models here.

class S2(models.Model):
    s2_accounts = models.TextField()
    s2_group = models.TextField()
    token = models.TextField()


    class Meta:
        db_table = "s2"