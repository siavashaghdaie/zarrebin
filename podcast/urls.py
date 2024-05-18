from django.urls import path
from . import views

urlpatterns = [
    
    path('login/' , views.loginPage, name="login"),
    path('logout/' , views.logoutUser, name="logout"),
    path('' , views.index, name="index"),
    #path('me/<str:pk>', views.me, name='me'),
    path('main/', views.main, name='main'),
    path('archive/', views.archive, name='archive'),
    path('podcasters/', views.podcasters, name='podcasters'),
    path('podcast-form/', views.podcastForm, name='podcast-form'),
    path('podcast-edit/<str:pk>/',views.podcastEdit, name="podcast-edit"),
    path('podcast-delete/<str:pk>/',views.podcastDelete, name="podcast-delete"),
    path('sp/', views.sp, name='sp'),
    path('team/', views.team, name='team'),
]