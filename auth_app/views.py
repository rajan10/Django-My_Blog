from django.shortcuts import render, redirect
from .forms import UserForm

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.



# 2 basic : login / logout
# 1 register_user

def register(request):
    if request.method=="GET":
        form=UserForm()
        context = {}
        context['form']=form
        return render(request, template_name="register.html", context=context)

    if request.method=="POST":
        form=UserForm(request.POST)

        if form.is_valid():
            # coz form is coming model no need to clean: and it goes auto to db only in model form only
            form.save()
            return redirect("/")

def Login(request):
    if request.method=="GET":
        # AuthenticatoinForm is the django's default authentication form that has username and password
        form=AuthenticationForm()
        context={}
        context['form']=form
        return render(request, template_name="login.html", context=context)
    if request.method=="POST":
        print(request.POST)
        # data=request.POST is the explicit way of fetching data from post form
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            # check where the interpreter is going in the python console
            print("form valid")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # check into the db if the user /password is matching: authenticate
            user = authenticate(username=username, password=password)
            if user is not None:
                # django's default login(arg1, arg2)
                login(request, user)
                return redirect('/')

        else:
            print("if form is invalid")
            return redirect('/login')



def Logout(request):
    logout(request)
    return redirect('/')


