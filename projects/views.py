from django.shortcuts import redirect, render
from .forms import CreateUserForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.
def registerPage(request):
    form=CreateUserForm()

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('index')

    context={'form':form}
    return render(request,'registration/registration_form.html',context)

@login_required(login_url='/accounts/login')
def index(request):
    return render(request,'index.html')

def profileView(request):
    logged_in_user=request.user #logged in user
    user=UserProfile.objects.get(user=logged_in_user)
    print(user)
    ctx={
        "user":user
    }
    return render(request,'profile.html',ctx)
