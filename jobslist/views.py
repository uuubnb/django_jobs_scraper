from django.shortcuts import render
import datetime

def home_page(request):
    date = datetime.datetime.now().date()
    name = 'Dave'
    _context = {'date': date, 'name': name}
    return render(request, 'home.html', _context)