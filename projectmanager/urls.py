from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='projectmanager/index.html')),
    path('add_project/', views.addProject, name='add-product' ),
    path('browse/', views.listProjects, name='browse' ),
]