from django.db import models
from django.conf import settings
from django.shortcuts import reverse

CATEGORY_CHOICES = (
    ('men', 'Men'),
    ('women', 'Women')
)

SUB_CATEGORY = (
    ('Shirts', 'Shirts'),
    ('Dress', 'Dresses'),
    ('Jeans', 'Jeans'),
    ('Shoes', 'Shoes'),
    ('purse', 'Purse')
)
LABELS = (
    ('Hot', 'hot'),
    ('New', 'new'),
    ('Sale', 'sale')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    discount_price = models.DecimalField(max_digits=10,decimal_places=2,null=True, blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=5)
    sub_category = models.CharField(choices=SUB_CATEGORY, max_length=6)
    label = models.CharField(choices=LABELS, null=True,
                             blank=True, max_length=4)
    description = models.CharField(max_length=2000)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shop:product", kwargs={
            'pk': self.id,
            'slug': self.slug
        })

    def get_cart_url(self):
        return reverse("shop:add_to_cart", kwargs={
            'pk': self.id,
            'slug': self.slug
        })
    
    def remove_from_cart_url(self):
        return reverse("shop:remove_from_cart", kwargs={
            'pk': self.id,
            'slug': self.slug
        })

    def remove_single_item_from_cart_url(self):
        return reverse("shop:remove_single_item_from_cart", kwargs={
            'pk': self.id,
            'slug': self.slug
        })

    def single_item_add_to_cart_url(self):
        return reverse("shop:single_item_add_to_cart", kwargs={
            'pk': self.id,
            'slug': self.slug
        })


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item.title}'

    def get_total_price(self):
        return float(self.quantity * self.item.price)
    
    def get_total_discount_price(self):
        return float(self.quantity * self.item.discount_price)

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_price()
        return self.get_total_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    ordered_date = models.DateTimeField()

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        
        return total
