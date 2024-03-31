from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from .models import Subject
from .forms import SubjectForm, SummarieForm 

# Create your views here.

class HomeView(View):
    def get(self, request):
        subjects = None
        if request.user.is_active:
            subjects = Subject.objects.filter(user=request.user).values()
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
        data = {"form": form, "error": "Algum erro ocorreu, tente novamente"}
        return render(request, "summaries/create_subject.html", data)


class UpdateSubject(View):
    def get(self, request, id):
        form = SubjectForm()
        return render(request, "summaries/update_subject.html", {"form": form, "id": id})
    
    def post(self, request, id):
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = Subject.objects.get(id=id)
            subject.name = form.cleaned_data["name"]
            subject.save()
            return redirect("summaries:home")
        data = {"form": form, "error": "Algum erro ocorreu, tente novamente "}
        return render(request, "summaries/update_subject.html", data)
            

class CreateSummarie(View):
    def get(self, request):
        form = SummarieForm(user=request.user)
        return render(request, "summaries/create_summarie.html", {'form': form})

    def post(self, request):
        form = SummarieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("summaries:home")
        data = {"form": form, "error": "Something went wrong"}
        return render(request, "summaries/create_summarie.html", data)


class ListSummaries(View):
    def get(self, request):
        return render(request, "summaries/summaries.html")

