from django.urls import path
#from community.views import write, articleList, viewDetail
from community import views

app_name = "community"
urlpatterns = [

    # path('write/', write, name='write'),
    # path('list/', articleList, name='article_list'),
    # #/view_detail/1/
    # path('view_detail/<int:num>/', viewDetail, name='view_detail'),    
    path('write/', views.WriteFormView.as_view(), name='write'),
    path('list/',  views.ArticleListView.as_view(), name='article_list'),
    #/view_detail/1/
    path('view_detail/<slug:pk>/', views.ArticleDetailView.as_view(), name='view_detail'),    
    
]
