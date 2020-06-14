from django.contrib import admin
from django.urls import path
from .views import test_view
from scraping.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_view),
    path('home/', home_view),
]
