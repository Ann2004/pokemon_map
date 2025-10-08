from django.db import models  # noqa F401
from django.utils.timezone import localtime

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="pokemons", blank=True)
    title_en = models.CharField(max_length=200, blank=True)
    title_jp = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    evolved_from = models.ForeignKey("self", models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, 
        on_delete=models.CASCADE,
        related_name='entities'
        )
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(default=localtime())
    disappeared_at = models.DateTimeField(default=localtime())
    level = models.IntegerField(blank=True, default=0)
    health = models.IntegerField(blank=True, default=0)
    strength = models.IntegerField(blank=True, default=0)
    defence = models.IntegerField(blank=True, default=0)
    stamina = models.IntegerField(blank=True, default=0)