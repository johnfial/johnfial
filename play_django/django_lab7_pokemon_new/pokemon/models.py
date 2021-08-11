from django.db import models
from django.contrib.auth import get_user_model

# consider adding an ImageField, per https://docs.djangoproject.com/en/3.2/ref/models/fields/#imagefield &  https://www.geeksforgeeks.org/imagefield-django-models/

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.URLField()
    image_back = models.URLField()
    caught_by = models.ManyToManyField(get_user_model(), related_name='caught') # odd that here, Nick's required blank=True
    # types = the set of Types associated with that Pokemon

    def __str__(self):
        return self.name
    
    # # just for fun, FAILED ATTEMPT to add the density field here, ~10-min and switching to doing it in the views.py or serializers.py
    # density = models.FloatField(default=(weight)/(height))
    
    # def __init__(self):
    #     self.calc_density(self)

    # def calc_density(self):
    #     self.density = self.weight/self.height

class Type(models.Model):
    type = models.CharField(max_length=50)
    pokemon = models.ManyToManyField(Pokemon, related_name='types')

    def __str__(self):
        return self.type