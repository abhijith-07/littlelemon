from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<pk>/', views.SingleMenuItemView.as_view()),
]