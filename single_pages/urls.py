from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.about_me),
    path('', views.landing),
]