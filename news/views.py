from django.shortcuts import render
from .models import News as NewsModel

# Create your views here.

def News(request):
    newss = NewsModel.objects.all().order_by("-date")
    return render(request, "news.html", {"newss": newss})