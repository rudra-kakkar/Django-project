from django.urls import path
from . import views

urlpatterns = [
    path('', views.toffee_list, name="toffee_list" ),
    path('create/', views.toffee_create, name="toffee_create" ),
    path('<int:toffee_id>/edit/', views.toffee_edit, name="toffee_edit" ),
    path('<int:toffee_id>/delete/', views.toffee_del, name="toffee_del" ),
    path('register/', views.register, name="register" ),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact")

    ]