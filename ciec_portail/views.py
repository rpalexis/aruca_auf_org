from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ciec_home(request):
    return render(request,'ciec_pages/accueil.html',{})


def candidature_ciec(request):
    return render(request,'ciec_pages/form_candidats.html',{})


def candidature_instance(request):
    return render(request,'ciec_pages/form_instances.html',{})
