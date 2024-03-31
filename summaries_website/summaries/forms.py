from django import forms
from .models import Subject, Summarie

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["name"]


class SummarieForm(forms.ModelForm):
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())

    def __init__(self, *args, user=None, **kwargs):
        super(SummarieForm, self).__init__(*args, **kwargs)
        if user:
            self.fields["subject"].queryset = Subject.objects.filter(user=user)


    class Meta:
        model = Summarie
        fields = ("subject", "title", "text")


