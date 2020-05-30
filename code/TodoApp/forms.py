from django import forms
from .models import TodoDb

class TodoForm(forms.ModelForm):
    class Meta:    
        model = TodoDb
        fields = ("task", "priority","completed", "description")