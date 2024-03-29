from django.contrib import admin
from django.urls import path, include

from todoapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<int:id>/',views.delete, name="delete"),
    path('update/<int:id>/',views.update, name="update"),

    path('cbvhome/', views.TaskListView.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.TaskDetailView.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cbvdelete'),
]