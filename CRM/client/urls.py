from django.urls import path
from . import views 

urlpatterns = [
    path('', views.clients_list, name='clients_list'),
    path('<int:id>/', views.clients_detail, name='clients_detail'),
    path('<int:id>/delete', views.delete_client, name='clients_delete'),
    path('<int:id>/edit', views.mod_client, name='clients_mod'),
    path('add/', views.create_client, name='clients_add'),
]