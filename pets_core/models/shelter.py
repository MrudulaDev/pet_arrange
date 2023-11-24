from django.db import models


class Shelter(models.Model):
    shelter_id = models.IntegerField()
    name = models.CharField(max_length=50)
    user_id = models.CharField(max_length=255)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
