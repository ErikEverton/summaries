from django.shortcuts import render
from django.views import View
from users.forms import RegisterForm, LoginForm

# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "users/register.html", {"form": form})
    
    def post(self, request):
        pass



class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})

