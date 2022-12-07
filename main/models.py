from django.db import models


CLOTHES_TYPES = [
    ('man', 'Мужской'),
    ('woman', 'Женский'),
    ('kid', 'Детский'),
    ('uni', 'Универсальный'),
]


SEASON_TYPES = [
    ('winter', 'Зима'),
    ('spring', 'Весна'),
    ('summer', 'Лето'),
    ('autumn', 'Осень'),
]


class Category(models.Model):
    category_name = models.CharField(verbose_name='Название категории', max_length=100)
    category_description = models.TextField()
    category_slug = models.SlugField(max_length=100, unique=True)


    def __str__(self):
        return self.category_name




class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    brand_description = models.TextField()
    brand_slug = models.SlugField(max_length=100, unique=True)


class Clothes(models.Model):
    clothes_name = models.CharField(max_length=100)
    clothes_description = models.TextField()
    clothes_slug = models.SlugField(max_length=100, unique=True)
    clothes_type = models.CharField(max_length=10, choices=CLOTHES_TYPES)
    clothes_season = models.CharField(max_length=10, choices=SEASON_TYPES)
    clothes_price = models.DecimalField(max_digits=10, decimal_places=2)
    clothes_image = models.ImageField(upload_to='clothes')
    clothes_brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='clothes')
    clothes_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='clothes')

    def __str__(self):
        return self.clothes_name

    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежда'
