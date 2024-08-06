# myapp/urls.py
from django.urls import path
from .views import register, login, list_items ,create_item, get_item, update_item, delete_item

urlpatterns = [
     path('register/', register),
    path('login/', login),
    path('items/', list_items, name='list_items'),
    path('items/create/', create_item, name='create_item'),
    path('items/<str:pk>/', get_item, name='get_item'),
    path('items/<str:pk>/update/', update_item, name='update_item'),
    path('items/<str:pk>/delete/', delete_item, name='delete_item'),
]
