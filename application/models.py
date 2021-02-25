from django.db import models
from django.contrib.auth.models import User

MONTH = (
    (1, 'JAN'),
    (2, 'FEB'),
    (3, 'MAR'),
    (4, 'APR'),
    (5, 'MAY'),
    (6, 'JUN'),
    (7, 'JUL'),
    (8, 'AUG'),
    (9, 'SEP'),
    (10, 'OCT'),
    (11, 'NOV'),
    (12, 'DEC')
)

DEALSIZE = (
    ('Small', 'Small'),
    ('Large', 'Large'),
    ('Medium', 'Medium')
)

class sales(models.Model):
    order_number = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    price = models.CharField(max_length=50)
    sales = models.CharField(max_length=50)
    month = models.CharField(max_length=2)
    year = models.PositiveIntegerField(max_length=4)
    productline = models.CharField(max_length=100)
    dealsize = models.CharField(max_length=20, choices=DEALSIZE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.order_number)