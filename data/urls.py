from django.urls import path,include
from . import views

urlpatterns = [
    path('clients', views.GetClients.as_view()),
    path('client', views.SaveClient.as_view()),
    path('categories', views.GetCategories.as_view()),


]
