from django.db import models


class Setup(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Run(models.Model):
    setup = models.ForeignKey(Setup, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    master_workers = models.IntegerField(default=0)
    node1_workers = models.IntegerField(default=0)
    node2_workers = models.IntegerField(default=0)
    node_swap_gb = models.IntegerField(default=0)
    cpu_time = models.FloatField(default=0)
    real_time = models.FloatField(default=0)

    def __str__(self):
            return self.name
