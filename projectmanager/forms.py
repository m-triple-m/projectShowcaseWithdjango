from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    """Form definition for Project."""

    class Meta:
        """Meta definition for Projectform."""

        model = Project
        fields = '__all__'
