from django.shortcuts import render
from .models import Profile, Project, Language
def index(request):
    '''
    Displays Landing Page
    '''
    profile = Profile.objects.get(pk=1)
    projects = Project.objects.all()
    languages = Language.objects.all()

   
    return render(request, "index.html",{"profile":profile,"projects": projects, "languages": languages})

# def projects(request):
#     '''
#     Displays projects
#     '''
    

#     return render(request, "projects.html",{"projects": projects})
