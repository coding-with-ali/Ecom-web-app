from django.urls import path
from backend.base.views.order_views import getOrderById
from base.views import order_views as  views



urlpatterns=[
    path('add/',views.addOrderItems, name='orders-add')
    path('<str:pk>/',views.getOrderById, name='user-order')

]