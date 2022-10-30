from django.db import models


class List(models.Model):
    name = models.CharField(max_length=50)


class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # relation with foreign key below
    # EACH Card must belong to a list
    list = models.ForeignKey(List, related_name='cards', on_delete=models.CASCADE)
    story_points = models.IntegerField(null=True, blank=True)
    business_value = models.IntegerField(null=True, blank=True)
