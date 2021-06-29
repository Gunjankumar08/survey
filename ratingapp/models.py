from django.db import models

class CustomerReview(models.Model):

    created = models.DateField(auto_now_add = True)
    prductRating = models.CharField(max_length=10 , null = True)
    priceRating = models.CharField(max_length=10 , null = True)
    purchaseRating = models.CharField(max_length=10 , null = True)
    recommendRating = models.CharField(max_length=10 , null = True)
    service = models.CharField(max_length=1000 , null = True)
