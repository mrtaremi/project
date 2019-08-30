from django.db import models


class State(models.Model):
    """Database Model for States"""
    name = models.CharField(max_length=100)
    en_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'استان {self.name}'

    class Meta:
        unique_together = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=40)
    en_name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name',)


class PlaceImage(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام")
    image = models.ImageField(upload_to='img/', default='img/no-img.png')

    def __str__(self):
        return self.name


class Place(models.Model):
    """Database Model for Places"""
    name = models.CharField(max_length=50, verbose_name="نام")
    thumb = models.ImageField(upload_to="img/")
    image = models.ManyToManyField(PlaceImage)
    desc = models.TextField(blank=True, null=True)
    url = models.URLField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name="موضوع")
    state = models.ForeignKey("State", on_delete=models.CASCADE, verbose_name="استان")

    # magic function
    def __str__(self):
        return self.name

    # part of models
    class Meta:
        unique_together = ('name',)
