from django.db import models

# Create your models here.

class Wyjazd(models.Model):
    nazwa       = models.CharField (max_length=300)
    data_wy     = models.DateTimeField (default=False)
    czas_do     = models.DecimalField (decimal_places=2,max_digits=10)
    czas_po     = models.DecimalField (decimal_places=2,max_digits=10)
    data_po     = models.DateTimeField (default=False)
    osoby       = models.CharField (max_length=500)
    samochod    = models.CharField (max_length=20, blank=True)
    j_sniadanie  = models.IntegerField()
    j_obiad      = models.IntegerField()
    j_kolacja    = models.IntegerField()

