from django.contrib import admin
from .models import Tag, Project, ProjectImage, Concept, Aptitude, ConceptImage, AptitudeImage, About, AboutImage, MonPDF, SecondPdf

# Register your models here.

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ConceptImageInline(admin.TabularInline):
    model = ConceptImage
    extra = 1

class AptitudeImageInline(admin.TabularInline):
    model = AptitudeImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "link")
    inlines = [ProjectImageInline]
    search_fields = ("title", "description")
    list_filter = ("tags",)

class ConceptAdmin(admin.ModelAdmin):
    inlines = [ConceptImageInline]

class AptitudeAdmin(admin.ModelAdmin):
    inlines = [AptitudeImageInline]
    


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(AptitudeImage)
admin.site.register(ConceptImage)
admin.site.register(Concept, ConceptAdmin)
admin.site.register(SecondPdf)
admin.site.register(Aptitude, AptitudeAdmin)
admin.site.register(About)
admin.site.register(AboutImage)
admin.site.register(MonPDF)



