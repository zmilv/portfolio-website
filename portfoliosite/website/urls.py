from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('projects/', views.projects, name='projects'),
    path('<int:project_id>/', views.detail, name='detail'),
    path('experience/', views.experience, name='experience'),
    path('education/', views.education, name='education'),
    path('other/', views.other, name='other'),
    path('contacts/', views.contacts, name='contacts'),
]
