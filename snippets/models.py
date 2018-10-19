
from django.db import models


# Create your models here.
class Snippets(models.Model):
    song = models.TextField()
    singer = models.TextField()
    token = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "snippets"
