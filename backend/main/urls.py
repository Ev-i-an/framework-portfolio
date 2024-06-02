from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("project/<int:id>/", views.project, name="project"),
    path("venue_pdf/<int:id>/", views.venue_pdf, name='venue_pdf'),
    path("pdf_divers/<int:id>/", views.pdf_divers, name='pdf_divers'),
    path("mentions/", views.mentions, name="aiblog")
]