from django.urls import path
from . import views


urlpatterns = [
    path('',views.accueil,name='accueil'),
    path('page', views.page, name='page'),
    path('update/<int:pk>',views.updateuser,name='update-user'),
    path('inscription',views.inscription,name='inscription'),
    path('delete/<int:pk>',views.deleteuser, name='delete-user'),
    
]