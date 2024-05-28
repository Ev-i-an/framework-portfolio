from django.shortcuts import render, get_object_or_404
from .models import Project, Tag, Aptitude


def home(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    aptitudes = Aptitude.objects.all() 
    return render(request, "home.html", {"projects": projects, "tags": tags, "aptitudes": aptitudes})


def contact(request):
    return render(request, "aiblog.html")


def aptitude(request):
    aptitudes = Aptitude.objects.all()
    context = {
        "aptitudes": aptitudes,
    }
    return render(request, "home.html", context)


def project(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, "project.html", {"project": project})
