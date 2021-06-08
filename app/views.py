from django.shortcuts import render
from .models import Login
from .forms import LoginForm

def index(request):

    context = {
        'name' : 'Bakr',
        'age' : 53425234525239662158,
    }

    return render(request,'pages/index.html',context)

def detail(request):

    if request.method == 'POST' :
        data = LoginForm(request.POST)
        if data.is_valid():
            data.save()

    context = {
        'login_form' : LoginForm
    }

    return render(request,'pages/detail.html',context)