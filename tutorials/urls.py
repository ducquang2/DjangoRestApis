from django.conf.urls import url 
from tutorials import views 
from django.urls import path

# from tutorials.core import views
 
urlpatterns = [ 
    url(r'^api/tutorials$', views.tutorial_list),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/tutorials/published$', views.tutorial_list_published),
    path('hello/', views.HelloView.as_view(), name='hello')
]