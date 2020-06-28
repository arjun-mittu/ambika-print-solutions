from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.db.models import Sum
from django.shortcuts import reverse
from django_countries.fields import CountryField
CATEGORY_CHOICES = (
    ('TS', 'TShirt'),
    ('SW', 'Sport wear'),
    ('CW', 'Casual wear'),
    ('DM','designer masks'),
    ('PPE','PPE kits')
)
TYPE_CHOICE=(
    ('TS','Track suits'),
    ('L','Lowers'),
    ('S','Shorts'),
    ('CTS','Cotton t-shirt'),
    ('STS','Sublimation t-shirt'),
    ('ML','Mask for ladies'),
    ('MM','Mask for men'),
    ('MU','Medical Use')
)
class Item(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    typechoice = models.CharField(choices=TYPE_CHOICE, max_length=3)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("core:products", kwargs={
            'slug': self.slug
        })
