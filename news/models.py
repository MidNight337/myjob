from distutils.command.upload import upload
from email.mime import image
from pyexpat import model
from statistics import mode
from unicodedata import category
from venv import create
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User

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
    
class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE) 
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'articles/')
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, 
                                related_name='post', 
                                on_delete=models.SET_NULL, 
                                null = True)
    tags = models.ManyToManyField(Tag, related_name='post')

class Recipe(models.Model):
    name = models.CharField(max_length=150)
    serves = models.CharField(max_length=57)
    prep_time = models.PositiveIntegerField(default = 0)
    cook_time = models.PositiveIntegerField(default= 0)
    ingredients = models.TextField()
    direction = models.TextField()
    post = models.ForeignKey(Post, related_name='recipe', on_delete=models.SET_NULL, null=True, blank=True)
    