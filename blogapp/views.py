from django.shortcuts import render
from blogapp.forms import RegistrationForm

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def registation(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'register.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request,'register.html',{'form': form})

def user_login(request):

    return render(request,'login.html',{})