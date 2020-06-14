from django.shortcuts import render
import datetime

def test_view(request):
    date = datetime.datetime.now().date()
    name = 'Dave'
    _context = {'date': date, 'name': name}
    return render(request, 'test.html', _context)