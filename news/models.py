from statistics import mode
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Category(MPTTModel):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    parent = TreeForeignKey(
        'self',
        related_name = 'children',
        on_delated  = models.SET_NULL,
        null =True,
        blank = True
    )

    class MPTTMeta:
        order_insertion_by = ['name']

class Tag(models.Model):
    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    