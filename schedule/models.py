from django.db import models


DAY_WEEK_CHOICES = [
    ('m', 'monday'),
    ('t', 'tuesday'),
    ('w', 'wednesday'),
    ('t', 'thursday'),
    ('f', 'friday'),
    ('sa', 'saturday'),
    ('su', 'sunday'),
]

NUM_OR_DEN_CHOICES = [
    ('n', 'numerator'),
    ('d', 'denominator'),
]


class Item(models.Model):
    name = models.CharField()
    teacher = models.CharField()
    start = models.CharField()
    end = models.CharField()
    day_of_the_week = models.CharField(choices=DAY_WEEK_CHOICES)
    num_or_den = models.CharField(choices=NUM_OR_DEN_CHOICES)
    coors = models.CharField()
    subgroup = models.CharField()

