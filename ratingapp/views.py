from django.shortcuts import render
from ratingapp.models import *
from django.http.response import HttpResponse

def home(request):
    return render(request,'welcome.html')

def RatingView(request):
    if request.method == "POST":
        # fform=FeedbackForm(request.POST)
        # print(request.POST)
        # if fform.is_valid():

        prductRating=request.POST.get('prductRating')
        priceRating=request.POST.get('pricesRating')
        purchaseRating=request.POST.get('purchaseRating')
        recommendRating=request.POST.get('recommendRating')
        service=request.POST.get('textdata')

        print(service,"service")
        print(prductRating,"prductRating")
        print(priceRating,"priceRating")
        print(purchaseRating,"purchaseRating")
        print(recommendRating,"recommendRating")

        data=CustomerReview(
            prductRating=prductRating,
            priceRating=priceRating,
            purchaseRating=purchaseRating,
            recommendRating=recommendRating,
            service=service,

            )
        data.save()
        return render(request,'thanku.html')

    else:
        return render(request,'rating.html')
