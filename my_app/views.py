from django.http import response
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from . import models
from requests.compat import quote_plus

BASE_CRAIGSLIST_URL = "https://delhi.craigslist.org/search/?query={}"

# Create your views here.
def home(request):
    return render(request, 'index.html')

def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    print(data)
    final_postings = []
    stuff_for_frontend = {
        'search': search,
        'final_postings': final_postings,

    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)