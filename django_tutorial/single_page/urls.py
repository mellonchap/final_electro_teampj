from django.urls import path
from .views import index, aboutMe, proJect, port

app_name = "single_page"
urlpatterns = [
    path('',aboutMe , name='index'),
    path('aboutme/',aboutMe , name='aboutMe'),
    path('project/',proJect , name='project'),
    path('port/',port , name='port'),
]
