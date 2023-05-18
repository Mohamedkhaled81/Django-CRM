from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_leads, name='list_leads'),
    path('create/', views.create_lead, name='create_lead'),
    path('<int:id>/', views.detail_lead, name='detail_lead'),
    path('<int:id>/modify', views.mod_lead, name='mod_lead'),
    path('<int:id>/delete', views.delete_lead, name='delete_lead'),
    path('<int:id>/convert', views.convert_to_client, name='convert_lead'),
]