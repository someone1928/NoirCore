from django import forms
from .models import Project, Note

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'file']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['content']
