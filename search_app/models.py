from django.db import models


class Search(models.Model):
    search = models.CharField(max_length=100000000)

    def __str__(self):
        return self.search