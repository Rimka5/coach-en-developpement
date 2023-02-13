from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home (request):
    return render(request, 'coach_rdv/home.html')

def registre (request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            mon_utilisateur = User.objects.create()
            mon_utilisateur.username = username
            mon_utilisateur.email = email
            mon_utilisateur.password = password1
            mon_utilisateur.password = password2
            mon_utilisateur.save()
        messages.success(request, 'votre compte a bien été crée avec succès')
        return redirect('login')
        
        
    return render(request, 'coach_rdv/registre.html')


def login (request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            print("TEST")
            login(request, user)
            username = user.username
            return render(request, 'coach_rdv/home.html', {'username':username})
        else:
            messages.error(request, 'le site n a pas pu vous authentifier')
            return redirect ('login')
    return render(request, 'coach_rdv/login.html')

def logout (request):
    pass
class LoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True