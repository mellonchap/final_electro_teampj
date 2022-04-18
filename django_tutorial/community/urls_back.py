from os import path
from community.views import write, articleList, viewDetail
from community import views

app_name = "community"
urlpatterns = [

    path('write/', write, name='write'),
    path('list/', articleList, name='article_list'),
    #/view_detail/1/
    path('view_detail/<int:num>/', viewDetail, name='view_detail'),    
]
