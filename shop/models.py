from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Product(models.Model):
    class PriceTypes(models.TextChoices):
        s = "$", "USD"
        sum = "So'm", "UZS"

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    price_type = models.CharField(max_length=30, choices=PriceTypes.choices, default=PriceTypes.sum)
    image = models.ImageField(upload_to='media/product')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    reyting = models.IntegerField()
    kg = models.IntegerField()

    def __str__(self):
        return f"{self.name}  {self.description}"


class Savat(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class Profession(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/testimonial')
    reyting = models.IntegerField()
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


