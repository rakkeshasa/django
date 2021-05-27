from django.db import models

class IntelCpu(models.Model):
    product_title = models.CharField(max_length = 200)
    product_price = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.product_title}: {self.product_price}'

class amdCpu(models.Model):
    product_title = models.CharField(max_length = 200)
    product_price = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.product_title}: {self.product_price}'

class nvidia(models.Model):
    product_title = models.CharField(max_length = 200)
    product_price = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.product_title}: {self.product_price}'

class ram(models.Model):
    product_title = models.CharField(max_length = 200)
    product_price = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.product_title}: {self.product_price}'

class radeon(models.Model):
    product_title = models.CharField(max_length = 200)
    product_price = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.product_title}: {self.product_price}'

class hdd(models.Model):
    product_title = models.CharField(max_length = 200)
    product_price = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.product_title}: {self.product_price}'

class ssd(models.Model):
    product_title = models.CharField(max_length = 200)
    product_price = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.product_title}: {self.product_price}'

class intelMB(models.Model):
    product_title = models.CharField(max_length = 200)
    product_price = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.product_title}: {self.product_price}'

class amdMB(models.Model):
    product_title = models.CharField(max_length = 200)
    product_price = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.product_title}: {self.product_price}'
# Create your models here.
