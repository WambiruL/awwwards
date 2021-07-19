from django.shortcuts import redirect, render
from .forms import CreateUserForm, UserUpdateForm,ProfleUpdateForm,ProjectUploadForm,VotesForm
from django.contrib.auth.models import User
from .models import UserProfile,Projects, Rates
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from .serializer import UserProfileSerializer,ProjectsSerializer
from django.http import Http404
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404

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
    myProjects = Projects.objects.all()
    return render(request,'index.html', {'myProjects':myProjects})


def profileView(request):
    logged_in_user=request.user #logged in user
    user=UserProfile.objects.get(user=logged_in_user)
    myProjects = Projects.objects.filter(profile=request.user)
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
        "myProjects":myProjects,
        'u_form':u_form,
        'p_form':p_form
    }
   
    return render(request,'profile.html',ctx)

@login_required(login_url='/accounts/login')
def submitSite(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectUploadForm(request.POST, request.FILES)
        if form.is_valid():
            home = form.save(commit=False)
            home.profile =current_user
            form.save()
        return redirect('index')
    else:
        form =ProjectUploadForm()
            
    return render(request,'new_project.html',{"form":form,})


def search_results(request):

    if 'projects' in request.GET and request.GET["projects"]:
        search_term = request.GET.get("projects")
        searched_projects = Projects.search_by_projects(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message="You can have not searched for anything"

        return render(request, 'search.html', {'message':message})

class UserProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self,request,format=None):
        all_profiles = UserProfile.objects.all()
        serializers = UserProfileSerializer(all_profiles,many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = UserProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ProjectsList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self,request,format=None):
        all_projects = Projects.objects.all()
        serializers = ProjectsSerializer(all_projects,many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = ProjectsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

def rating(request, pk):
    
    project = get_object_or_404(Projects, pk=pk)
    current_user = request.user
    if request.method == 'POST':
        form = VotesForm(request.POST)
        if form.is_valid():
            design_rating = form.cleaned_data["design_rating"]
            usability_rating = form.cleaned_data["usability_rating"]
            content_rating = form.cleaned_data["content_rating"]
            comment = form.cleaned_data["comment"]
            rating = form.save(commit=False)
            rating.project = project
            rating.author = current_user
            rating.design_rating = design_rating
            rating.usability_rating = usability_rating
            rating.content_rating = content_rating
            rating.comment = comment
            rating.save()
            # return redirect('home')
    else:
        form = VotesForm()
    return render(request,'rating.html', {'project' : project, 'form' : form})   