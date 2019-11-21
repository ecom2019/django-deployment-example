from django.db import models
from django.utils.text import slugify

# Create your models here.

CATEGORY_CHOICES=(
    ('electronics','ELECTRONICS'),
    ('medicalequipments','MEDICAL_EQUIPMENTS'),
    ('books','BOOKS'),
    ('movies','MOVIES'),
)

LANGUAGE_CHOICES=(
    ('english','ENGLISH'),
    ('amharic','AMHARIC'),
)
STATUS_CHOICES=(
    ('RA','RECENTLY ADDED'),
    ('MW','MOST WATCHED'),
    ('TR','TOP RATED'),
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='products')
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=100)
    language = models.CharField(choices=LANGUAGE_CHOICES,max_length=20)
    status = models.CharField(choices=STATUS_CHOICES,max_length=2)
    manufacturer = models.CharField(max_length=100)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    
DOWNLOAD_CHOICES=(
    ('S','SPECIFICATIONS'),
    ('V','VIDEO'),
)
class DownloadLinks(models.Model):
    download = models.ForeignKey(Product, related_name='product_download_link', on_delete=models.CASCADE)
    type = models.CharField(choices=DOWNLOAD_CHOICES, max_length=1)
    link = models.URLField()
    
    def __str__(self):
        return self.download

