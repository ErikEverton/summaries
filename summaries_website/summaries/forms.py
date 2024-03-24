from django import forms
from .models import Subject, Summarie

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["name"]


class SummarieForm(forms.ModelForm):
    subject = forms.ChoiceField(
        queryset=Subject.objects.filter(),
        
    )
    class Meta:
        model = Summarie
        fields = ("subject", "title", "text")


