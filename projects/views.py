from django.shortcuts import redirect, render
from .forms import CreateUserForm

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

def index(request):
    return render(request,'index.html')
