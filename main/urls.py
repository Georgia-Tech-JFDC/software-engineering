from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('analytics-dashboard/', views.analytics_dashboard, name='analytics_dashboard'),
    path('rso-document-checker/', views.rso_document_checker, name='rso_document_checker'),
]

