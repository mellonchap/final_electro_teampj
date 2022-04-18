from django.contrib import admin

from dashboard import models

class CountryAdmin(admin.ModelAdmin):    
    list_display = ('country', 'population')
# Register your models here.

admin.site.register(models.CountryData, CountryAdmin)