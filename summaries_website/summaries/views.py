from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views import View
from .models import Subject

# Create your views here.

class HomeView(View):
    def get(self, request):
        subjects = Subject.objects.order_by('name')
        context = {"subjects": subjects}
        return render(request, 'summaries/index.html', context)


class CreateSubject(CreateView):
    model = Subject
    fields = ["name"]
    template_name = 'summaries/create_subject.html'

