from django.urls import path
from base import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('add_person/', views.add_person, name= 'add_person'),
    path('edit/<int:pk>/', views.edit_person, name= 'edit_person'),
    path('delete/<int:pk>/', views.delete_person, name= 'delete_person'),
    path('about/', views.about, name= 'about'),
]
