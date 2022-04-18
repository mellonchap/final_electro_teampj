from dataclasses import field
from django.contrib import admin

# Register your models here.
#from. import models
from community import models

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('제목', {'fields':['title']}),
        ('내용', {'fields':['contents']}),
        ('작성자 정보', {'fields':['name','url','email']}),
        ('작성자 ID', {'fields':['owner'], 'classes':['collapse']}),
    ]
    list_display = ('pk','title','url','cdate')
    list_filter = ['cdate']
    search_fields = ['title','contents']
admin.site.register(models.Article, ArticleAdmin)