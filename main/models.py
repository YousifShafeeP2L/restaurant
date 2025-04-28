from django.db import models


class Restaurant(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=200, null=True)
    image = models.CharField(max_length=255, null=True)
    rating = models.FloatField()

    def __str__(self):
        return self.title
