from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views import View
from .models import Subject
from .forms import SubjectForm 

# Create your views here.

class HomeView(ListView):
    template_name = 'summaries/index.html'
    model = Subject

    def get_queryset(self):
        user = self.request.user
        queryset = Subject.objects.filter(user=user)
        return queryset.order_by("name")


class CreateSubject(View):
    def get(self, request):
        form = SubjectForm()
        return render(request, "summaries/create_subject.html", {"form": form})

    def post(self, request):
        data = {"form": SubjectForm(), "error": "Algo deu errado tente novamente"}
