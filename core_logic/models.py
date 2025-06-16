from django.db import models
from django.urls import reverse

class currencyTypes(models.TextChoices):
    PAKISTANI_RUPEE = 'PKR', 'Pakistan Rupee'
    US_DOLLAR = 'USD', 'US Dollar'
    EURO = 'EUR', 'Euro'
    CANADIAN_DOLLAR = 'CAD', 'Canadian Dollar'
    RIYAL = 'SAR', 'Saudi Riyal'

class savingTypes(models.TextChoices):
    SAVINGS = 'SAVE', 'saved'
    LOSS = 'SPENT', 'used'

# Create your models here.
class Expense(models.Model):
    __tablename__ = 'expenses'
    id = models.AutoField(primary_key=True)

    name = models.TextField()
    type = models.CharField(max_length=7, choices=savingTypes, default=savingTypes.SAVINGS)

    price = models.FloatField()
    currency = models.CharField(max_length=3, choices=currencyTypes, default=currencyTypes.PAKISTANI_RUPEE)

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} --- |{self.date}| --- {self.currency} {self.price}'

    def get_absolute_url(self): # new
        return reverse("home")
