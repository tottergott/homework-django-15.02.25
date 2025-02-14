from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
class Donate(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=255,
    )
    sum = models.FloatField(
        validators=[MinValueValidator(0.0)],
        verbose_name='сумма',
        blank=True,
    )
    picture = models.ImageField(
        verbose_name='картинка',
        blank=True,
    )
   