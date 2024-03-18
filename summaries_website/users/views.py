from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from users.forms import RegisterForm, LoginForm

# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "users/register.html", {"form": form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            data = {'form': form, 'error': 'Error: Você provavelmente digitou algum valor errado'}
            return render(request, 'users/register.html', data)



class LoginView(View):
    def get(self, request):
        form = LoginForm(request.POST)
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, email=email, password=password)
            if user:
                login(request, user=user)
                return redirect("summaries:home")
        else:
            data = {'form': form, 'error': 'Error: Você provavelmente digitou o valor errado'}
            return render(request, 'auth/login.html', data) 


class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect("login")

