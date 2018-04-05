from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('timeclockindex/', views.index, name='timeclockindex' ),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('schedule/', views.schedule, name='schedule'),
    path('stopschedule/', views.stopschedule, name='stopschedule'),
]