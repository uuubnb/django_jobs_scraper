from django.shortcuts import render
from .models import Position

def home_view(request):
    qs = Position.objects.all()
    return render(request, 'scraping/home.html', {'object_list': qs})
