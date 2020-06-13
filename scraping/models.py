from django.db import models
from .utils import from_cyrillic_to_eng

class City(models.Model):
    city_name = models.CharField(max_length=50, verbose_name='Название города', unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Название города'
        verbose_name_plural = 'Названия городов'
    
    def __str__(self):
        return self.city_name   
    
    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.city_name)) #поскольку city_name - CharField а не str
        super().save(*args, **kwargs) 

class Speciality(models.Model):
    speciality_name = models.CharField(max_length=50, verbose_name='Название специальности', unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Название специальности'
        verbose_name_plural = 'Названия специальностей'
    
    def __str__(self):
        return self.speciality_name   
    
    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.speciality_name)) #поскольку city_name - CharField а не str
        super().save(*args, **kwargs) 

class Position(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Название вакансии')
    company = models.CharField(max_length=250, verbose_name='Имя компании')
    description = models.TextField(verbose_name='Полное описание вакансии')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город вакансии')
    speciality = models.ForeignKey('Speciality', on_delete=models.CASCADE, verbose_name='Специализация вакансии')
    added_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Название вакансии'
        verbose_name_plural = 'Доступные вакансии'
    
    def __str__(self):
        return self.title   


    