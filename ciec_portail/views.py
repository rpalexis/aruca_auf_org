from django.shortcuts import render
from django.http import HttpResponse

from .forms import InstanceCandidatureForm
# Create your views here.

def ciec_home(request):
    return render(request,'ciec_pages/accueil.html',{})


def candidature_ciec(request):
    form = InstanceCandidatureForm
    return render(request,'ciec_pages/form_candidats.html',{'form':form})


def candidature_instance(request):
    return render(request,'ciec_pages/form_instances.html',{})
