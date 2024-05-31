from django.shortcuts import render, get_object_or_404
from .models import Project, Tag, Aptitude, About, Concept, MonPDF
from django.http import FileResponse


def home(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    aptitudes = Aptitude.objects.all()
    about_object = About.objects.all()
    concept_object = Concept.objects.all()  
    return render(request, "home.html", {"projects": projects, "tags": tags, "aptitudes": aptitudes, "about_object": about_object, "concept_object": concept_object})

def concept_list(request):
    concept_object = Concept.objects.all() 
    context = {
        "concept_object": concept_object,
    }
    return render(request, "home.html", context)


def contact(request):
    return render(request, "aiblog.html")


def aptitude(request):
    aptitudes = Aptitude.objects.all()
    context = {
        "aptitudes": aptitudes,
    }
    return render(request, "home.html", context)

def about_list(request):
    about_object = About.objects.all() 
    context = {
        "about_object": about_object,
    }
    return render(request, "home.html", context)


def project(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, "project.html", {"project": project})

def venue_pdf(request, id):
    # Trouvez le bon PDF en fonction de l'ID
    pdf = MonPDF.objects.get(id=id)
    pdf_path = pdf.pdf.path

    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')


def pdf_divers(request, id):
    # Trouvez le bon PDF en fonction de l'ID
    pdf = MonPDF.objects.get(id=id)
    pdf_path = pdf.pdf.path

    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')


