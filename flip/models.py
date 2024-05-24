from django.db import models

class advertisement(models.Model):
    item=models.TextField(max_length=200)
    price=models.IntegerField()
    image=models.TextField(max_length=200)
    description=models.TextField(max_length=200)
    def __str__(self):
        return self.item
