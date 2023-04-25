from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    url = models.CharField(max_length=200, null=True, blank=True)
    named_url = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name