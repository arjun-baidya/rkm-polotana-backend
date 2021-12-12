from django.urls import path
import backend.views as views

urlpatterns = [
    path('news/', views.getNews, name='news'),
    path('events/', views.getEvents, name='events'),
    path('pujas/', views.getPujas, name='pujas'),
]