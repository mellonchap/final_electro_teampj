from django.urls import path
from .views import electro2 

app_name = "electro_project"
urlpatterns = [
    path('project_1/', electro2,  name='electro2'),
]

