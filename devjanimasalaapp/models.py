from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return (self.category_name)


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to="./products")
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    products_featured = models.BooleanField()
    product_details = models.TextField(max_length=1200)
    category = models.ForeignKey('Category' , on_delete=models.CASCADE, related_name='product')
    
    def __str__(self):
        return (self.product_name)

class Rating(models.Model):
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '8'
    RATINGS_CHOICES = [
        (ONE, '1'),
        (TWO, '2'),
        (THREE, '3'),
        (FOUR, '4'),
        (FIVE, '5'),
    ]
    product = models.ForeignKey('Product' , on_delete=models.CASCADE, related_name='rating')
    product_review = models.TextField(max_length=500)
    product_ratings = models.CharField(max_length=1, choices = RATINGS_CHOICES)

# Extra model
class Image(models.Model):
    name = models.CharField(max_length=255)
    image = ProcessedImageField(upload_to='images/', processors=[ResizeToFill(800, 400)])
    description = models.TextField()
