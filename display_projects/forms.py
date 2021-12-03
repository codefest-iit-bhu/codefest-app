from django import forms
from .models import ProjectModel


class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = ('title', 'description', 'link', 'screenshot')
