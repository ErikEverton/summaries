from django import forms
from .models import Subject

class SubjectForm(forms.Form):
    name = forms.CharField(max_length=30)
    class Meta:
        model = Subject
        fields = ["name"]


