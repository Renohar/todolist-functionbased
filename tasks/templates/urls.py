from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('',views.index,name = 'list'),
    path('update/<str:pk>',views.updateTask,name='update'),
    path('delete/<str:pk>',views.deleteTask,name='delete')
]