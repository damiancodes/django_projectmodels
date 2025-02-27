from django.urls import path
from myapp import views

urlpatterns = [

path('', views.index, name='index'),
path('post_details', views.post_details, name='post_details'),
]