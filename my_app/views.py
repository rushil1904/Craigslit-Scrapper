from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def new_search(request):
    search = request.POST.get('search')
    final_postings = []
    stuff_for_frontend = {
        'search': search,
        'final_postings': final_postings,

    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)