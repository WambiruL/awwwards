from django.shortcuts import redirect, render
from .forms import CreateUserForm, UserUpdateForm,ProfleUpdateForm
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
    
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfleUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        return redirect('profile')

    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfleUpdateForm(instance=request.user.userprofile)
    ctx={
        "user":user,
        'u_form':u_form,
        'p_form':p_form
    }
   
    return render(request,'profile.html',ctx)


