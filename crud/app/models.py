from django.db import models

class Item(models.Model):
    class Meta:
        db_table = 'item'
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name