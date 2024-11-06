from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TemplateView.as_view(template_name='projectmanager/index.html')),
    path('add_project/', views.addProject, name='add-product' ),
    path('browse/', views.listProjects, name='browse' ),
    path('project-details/<int:id>/', views.projectDetails, name='project-details' ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)