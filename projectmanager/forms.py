from django.forms import ModelForm
from .models import Project
from django import forms

class ProjectForm(ModelForm):
    """Form definition for Project."""

    class Meta:
        """Meta definition for Projectform."""

        model = Project
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(  attrs={'class': 'w-full bg-gray-300 rounded px-4 py-2 mb-6 text-black'}),
            'description': forms.Textarea(attrs={'rows': 5, 'class': 'w-full bg-gray-300 rounded px-4 py-2 mb-6 text-black'}),
            'department': forms.TextInput(attrs={'class': 'w-full bg-gray-300 rounded px-4 py-2 mb-6 text-black'}),
            'technology': forms.TextInput(attrs={'class': 'w-full bg-gray-300 rounded px-4 py-2 mb-6 text-black'}),
            'image': forms.FileInput(attrs={'class': 'w-full bg-gray-300 rounded px-4 py-2 mb-6 text-black'}),
            'student_name': forms.TextInput(attrs={'class': 'w-full bg-gray-300 rounded px-4 py-2 mb-6 text-black'}),
            'student_github': forms.URLInput(attrs={'class': 'w-full bg-gray-300 rounded px-4 py-2 mb-6 text-black'}),
            'student_linkedin': forms.URLInput(attrs={'class': 'w-full bg-gray-300 rounded px-4 py-2 mb-6 text-black'}),
            'student_email': forms.EmailInput(attrs={'class': 'w-full bg-gray-300 rounded px-4 py-2 mb-6 text-black'}),
            'student_avatar': forms.FileInput(attrs={'class': 'w-full bg-gray-300 rounded px-4 py-2 mb-6 text-black'}),
            'enrollment_number': forms.TextInput(attrs={'class': 'w-full bg-gray-300 rounded px-4 py-2 mb-6 text-black'}),
            
        }
        labels = {
            'title': 'Project Title'
        }
