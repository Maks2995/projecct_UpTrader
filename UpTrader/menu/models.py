from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=186, unique=True)
    slug = models.SlugField(max_length=186)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=186)
    slug = models.SlugField(max_length=186)
    menu = models.ForeignKey(Menu, blank=True, related_name='items', on_delete=models.CASCADE)
    parent = models.ForeignKey(Menu, blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
