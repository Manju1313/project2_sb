from django.db import models
import datetime
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import time,date
from django.forms import ModelForm


# Create your models here.
GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)
TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]



class people(models.Model):
    #title      = models.CharField(max_length=3, choices=TITLE_CHOICES)
    first_name =models.CharField(max_length=30)
    last_name  =models.CharField(max_length=30)
    #slug      = models.SlugField(max_length=200, db_index=True, unique = True)
    age        =models.PositiveIntegerField(null=True,blank=True)
    gender     = models.IntegerField(choices=GENDER_CHOICES)
    date       =models.DateField(null=True,blank=True)

    def __str__(self):
        return self.first_name


class marks(models.Model):
    first_name  =models.ForeignKey(people ,on_delete=models.CASCADE,null=True,blank=True)
    Telugu      =models.PositiveIntegerField(null=True,blank=True,validators=[MinValueValidator(0),MaxValueValidator(100)])
    English     =models.PositiveIntegerField(null=True,blank=True,validators=[MinValueValidator(0),MaxValueValidator(100)])
    Mathematics =models.PositiveIntegerField(null=True,blank=True,validators=[MinValueValidator(0),MaxValueValidator(100)])
    Biology     =models.PositiveIntegerField(null=True,blank=True,validators=[MinValueValidator(0),MaxValueValidator(100)])
    Physics     =models.PositiveIntegerField(null=True,blank=True,validators=[MinValueValidator(0),MaxValueValidator(100)])
    Chemistry   =models.PositiveIntegerField(null=True,blank=True,validators=[MinValueValidator(0),MaxValueValidator(100)])
    Social      =models.PositiveIntegerField(null=True,blank=True,validators=[MinValueValidator(0),MaxValueValidator(100)])
    def __str__(self):
        return self.first_name.first_name


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.SlugField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline



# class Topic(models.Model):
#     topic_name=models.CharField(max_length=100,primary_key=True)
#     date=models.DateField()


from operator import mod
from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    date=models.DateField()
