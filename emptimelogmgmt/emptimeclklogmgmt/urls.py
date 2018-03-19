from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('timeclockindex/', views.timeclockindex, name='timeclockindex' ),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register')
]