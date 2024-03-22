from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from .models import Subject
from .forms import SubjectForm 

# Create your views here.

class HomeView(View):
    def get(self, request):
        subjects = Subject.objects.all().values()
        print(subjects)
        return render(request, "summaries/index.html", {"subjects": subjects})

class CreateSubject(View):
    def get(self, request):
        form = SubjectForm()
        return render(request, "summaries/create_subject.html", {"form": form})

    def post(self, request):
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.user = request.user
            subject.save()
            return redirect("summaries:home")
        data = {"form": form, "error": "Algo deu errado tente novamente"}
        return render(request, "summaries/create_subject.html", data)
