from django.db import models

# Create your models here.
# https://azinkin.ru/orm.html

class Category(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=255,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'


class Post(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=255,
    )
    content = models.TextField(
        verbose_name='контент',
        blank=True,
    )
    picture = models.ImageField(
        verbose_name='картинка',
        blank=True,
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=False,
    )
    category = models.ForeignKey(
        verbose_name='категория',
        to='Category',
        on_delete=models.CASCADE,
    )

     
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'публикации'
        unique_together = ('category', 'slug')





class Comments(models.Model):
    category = models.ForeignKey(
        verbose_name='публикации',
        to='Post',
        on_delete=models.CASCADE,
    )
    content = models.TextField(
        verbose_name='имя',
        blank=True,
    )
    content = models.TextField(
        verbose_name='комментарий',
        blank=True,
    )
    date = models.DateTimeField(
        verbose_name='дата',
        blank=True,
    )
    parent = models.ForeignKey(
        verbose_name='родитель',
        to='Comments',
        on_delete=models.CASCADE,
    )

class Likes(models.Model):
    category = models.ForeignKey(
        verbose_name='публикации',
        to='Post',
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(
        verbose_name='дата',
        blank=True,
    )
    reaction = models.BooleanField(
        verbose_name='реакция',
    )
