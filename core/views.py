from django.shortcuts import render, redirect
from product.models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as dj_login
from django.contrib import messages

def home(request):
    products = Product.objects.all()[0:8]

    context = {
        'products': products,
        'home': 0
    }

    return render(request, 'core/content.html', context)

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Nom d'utilisateur existe déjà! Veuillez essayer un autre nom d'utilisateur")
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "E-mail déjà enregistré")
            return redirect('register')
        
        if len(username)>20:
            messages.error(request, "Le nom d'utilisateur doit comporter moins de 20 caractères")
            return redirect('register')
        
        if pass1 != pass2:
            messages.error(request, "Les mots de passe ne correspondent pas")
            return redirect('register')
        
        if len(pass1)<=8:
            messages.error(request, "Le mot de passe doit comporter moins de 8 caractères")
            return redirect('register')
        
        if not username.isalnum():
            messages.error(request, "Le nom d'utilisateur doit être alphanumérique")
            return redirect('register')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        
        return redirect('login')
        
    return render(request, "core/register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            dj_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Mot de passe incorrect")
            return redirect('login')
    
    return render(request, 'core/login.html')

def logout(request):
    logout(request)
    return redirect('login')

def faq(request):
    context = {
        'home': 0
    }

    return render(request, 'core/faq.html', context)

def contact(request):
    context = {
        'home': 0
    }

    return render(request, 'core/contact.html', context)

def aboutme(request):
    context = {
        'home': 0
    }

    return render(request, 'core/about-me.html', context)
