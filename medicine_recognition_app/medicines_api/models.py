from django.db import models

# Create your models here.


class Medicine(models.Model):
    category_name = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    effective_material = models.CharField(max_length=50, blank=True, null=True)
    en_name = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField(default=0)
    usage = models.TextField(max_length=250, blank=True, null=True)
    ar_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.id} --- {self.en_name}'
