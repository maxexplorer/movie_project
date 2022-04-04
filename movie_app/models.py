from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField(null=True, blank=True)
    slug = models.SlugField(default='', null=True, blank=True, db_index=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.last_name)
        super(Director, self).save(*args, **kwargs)


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Men'),
        (FEMALE, 'Woman'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS, blank=True)
    slug = models.SlugField(default='', null=True, blank=True, db_index=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.last_name)
        super(Actor, self).save(*args, **kwargs)


class Movie(models.Model):
    YES = 'Y'
    NO = 'N'
    RECOMMENDATION_CHOICES = [
        (YES, 'YES'),
        (NO, 'NO'),
    ]
    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000,
                                 validators=[MinValueValidator(1)])
    recommend = models.CharField(max_length=1, choices=RECOMMENDATION_CHOICES, default=YES)
    slug = models.SlugField(default='', null=False, db_index=True)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True, blank=True)
    actors = models.ManyToManyField(Actor)

    def get_url(self):
        return reverse('movie_detail', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}% - {self.budget} - {self.year} - {self.slug}'

# from movie_app.models import Movie
