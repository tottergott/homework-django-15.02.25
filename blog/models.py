from audioop import tomono

from django.db import models


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
    category = models.ForeignKey(
        verbose_name='категория',
        to='Category',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        verbose_name='название',
        max_length=255,
    )
    content = models.TextField(
        verbose_name='контент',
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=False,
    )
    picture = models.ImageField(
        verbose_name='изображение',
        blank=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'публикации'
        unique_together = ('category', 'slug')


class Like(models.Model):
    post = models.ForeignKey(
        verbose_name='публикация',
        to='Post',
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True,
    )
    reaction = models.IntegerField(
        verbose_name='реакция',
        choices=[
            (1, 'Лайк'),
            (-1, 'Дизлайк'),
        ],
    )

    def __str__(self):
        if self.reaction > 0:
            return f'+{self.reaction} {self.post}'
        return f'{self.reaction} {self.post}'

    class Meta:
        verbose_name = 'лайк'
        verbose_name_plural = 'реакции'


class Comment(models.Model):
    post = models.ForeignKey(
        verbose_name='публикация',
        to='Post',
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True,
    )
    name = models.CharField(
        verbose_name='имя',
        max_length=255,
    )
    text = models.TextField(
        verbose_name='комментарий',
    )
    parent = models.ForeignKey(
        verbose_name='родитель',
        to='self',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name} про "{self.post}"'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'обсуждение'


class Donat(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=255,
    )
    link = models.URLField(
        verbose_name='ссылка',
    )
    icon = models.ImageField(
        verbose_name='иконка',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сервис'
        verbose_name_plural = 'сервисы донатов'
