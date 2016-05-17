from django.shortcuts import render
from django.http import HttpResponse

from .forms import InstanceCandidatureForm,CandidatMembreForm
# Create your views here.

def ciec_home(request):
    return render(request,'ciec_pages/accueil.html',{})


def candidature_ciec(request):
    if request.method == 'POST':
        form = InstanceCandidatureForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponse('/thanks/')
        else:
            print("Non validee")
    else:
        form = InstanceCandidatureForm

    return render(request,'ciec_pages/form_candidats.html',{'form':form})





def candidature_instance(request):
    if request.method == 'POST':
        form = CandidatMembreForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponse('/thanks/')
        else:
            print("Non validee")
    else:
        form = CandidatMembreForm
    return render(request,'ciec_pages/form_instances.html',{'form':form})
