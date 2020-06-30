from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.db.models import Sum
from django.shortcuts import reverse
from django_countries.fields import CountryField
CATEGORY_CHOICES = (
    ('TShirt', 'TShirt'),
    ('Sport Wear', 'Sport wear'),
    ('Casual Wear', 'Casual wear'),
    ('Designer Masks','designer masks'),
    ('PPE kits','PPE kits')
)
TYPE_CHOICE=(
    ('Track Suit','Track suits'),
    ('Lowers','Lowers'),
    ('Shorts','Shorts'),
    ('Cotton T-Shirt','Cotton t-shirt'),
    ('Sublimation T-Shirt','Sublimation t-shirt'),
    ('Mask for Ladies','Mask for ladies'),
    ('Mask for Men','Mask for men'),
    ('Medical Use','Medical Use')
)
size_choice=(
    ('XXXL','XXXL'),
    ('XXL','XXL'),
    ('XL','XL'),
    ('L','L'),
    ('M','M'),
    ('S','S'),
    ('XS','XS'),
    ('XXS','XXS')
)

class Item(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    typechoice = models.CharField(choices=TYPE_CHOICE, max_length=50)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })
    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })
    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size=models.CharField(choices=size_choice,max_length=255)
    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
    def get_total_item_price(self):
        return self.quantity * self.item.price
    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price
    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()
    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey(
        'BillingAddress', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total
class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    city=models.CharField(max_length=255,null=True)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    email=models.EmailField(null=True)
    phoneno=models.IntegerField(null=True)
    def __str__(self):
        return self.user.username

class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Contactme(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(null=True)
    subject=models.CharField(max_length=255)
    message=models.CharField(max_length=255)
    def __str__(self):
        return self.name
