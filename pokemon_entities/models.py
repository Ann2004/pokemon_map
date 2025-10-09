from django.db import models  # noqa F401
from django.utils.timezone import now

class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name = "название")
    photo = models.ImageField(upload_to="pokemons",
                              verbose_name = "картинка"
                              )
    title_en = models.CharField(max_length=200, 
                                blank=True,
                                verbose_name = "название на английском"
                                )
    title_jp = models.CharField(max_length=200, 
                                blank=True,
                                verbose_name = "название на японском"
                                )
    description = models.TextField(blank=True, verbose_name = "описание")
    evolved_from = models.ForeignKey("self", 
                                     models.SET_NULL,
                                     related_name="evolve_to", 
                                     blank=True, 
                                     null=True,
                                     verbose_name = "предыдущая эволюция"
                                     )
    
    def __str__(self):
        return self.title
    
class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, 
        on_delete=models.CASCADE,
        related_name='entities',
        verbose_name = "покемон"
        )
    lat = models.FloatField(verbose_name = "широта")
    lon = models.FloatField(verbose_name = "долгота")
    appeared_at = models.DateTimeField(default=now, verbose_name = "время появления на карте")
    disappeared_at = models.DateTimeField(default=now, verbose_name = "время исчезновения на карте")
    level = models.IntegerField(blank=True, 
                                default=0,
                                verbose_name = "уровень"
                                )
    health = models.IntegerField(blank=True, 
                                 default=0,
                                 verbose_name = "здоровье"
                                 )
    strength = models.IntegerField(blank=True, 
                                   default=0,
                                   verbose_name = "атака"
                                   )
    defence = models.IntegerField(blank=True, 
                                  default=0,
                                  verbose_name = "защита"
                                  )
    stamina = models.IntegerField(blank=True, 
                                  default=0,
                                  verbose_name = "выносливость"
                                  )