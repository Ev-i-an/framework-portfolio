from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects")
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="project_images/")

    def __str__(self):
        return f"{self.project.title} Image"







class Concept(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class ConceptImage(models.Model):
    concept = models.ForeignKey(
        Concept, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="concept_images/")

    def __str__(self):
        return f"{self.concept.title} Image"

class SecondPdf(models.Model):
    conceptpdf = models.ForeignKey(
        Concept, related_name="pdfs", on_delete=models.CASCADE
    )
    pdf = models.FileField(upload_to='pdfs/') 

    def __str__(self):
        return f"PDF lié à : {self.conceptpdf.title}"




class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class AboutImage(models.Model):
    about = models.ForeignKey(
        About, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="about_images/")

    def __str__(self):
        return f"{self.about.title} Image"
    
class MonPDF(models.Model):
    aboutpdf = models.ForeignKey(
        About, related_name="pdfs", on_delete=models.CASCADE
    )
    pdf = models.FileField(upload_to='pdfs/') 

    def __str__(self):
        return f"PDF lié à : {self.aboutpdf.title}"   








class Aptitude(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class AptitudeImage(models.Model):
    aptitude = models.ForeignKey(
        Aptitude, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="aptitude_images/")

    def __str__(self):
        return f"{self.aptitude.title} Image"