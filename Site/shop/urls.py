from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('contacts/', views.contacts, name='contacts'),

    path('about_us/', views.about_us, name='about_us'),
]