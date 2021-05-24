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
    soup = BeautifulSoup(data,features='html.parser')
    post_listings = soup.find_all('li', {'class': 'result-row'})
    post_title = post_listings[0].find(class_='result-title').text
    post_url = post_listings.find('a').get('href')
    post_price = post_listings.find(class_='result-price').text
    print(data)
    final_postings = []
    stuff_for_frontend = {
        'search': search,
        'final_postings': final_postings,

    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)