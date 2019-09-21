from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from djangoapp.models import user
from djangoapp.forms import UserRegisterForm

def index(request):
    return render(request,'base.html')


def home(request):
    return render(request,'home.html')

def familydetails(request):
    id=request.user.id
    # print('//////',id)
    form=user.objects.filter(id=id)
    # print('===',form)
    return render(request,'family.html',{'form':form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})