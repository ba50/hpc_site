from django.db import models


class Setup(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Run(models.Model):
    setup = models.ForeignKey(Setup, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
            return self.name
