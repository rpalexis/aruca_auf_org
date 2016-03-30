# -*- encoding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import Context, RequestContext
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from appels.models import *


def appel_offre(request):
    item_list = Appel_Offre.objects.filter(status=3).order_by('-date_fin').reverse()
    return render_to_response('appel_offre.html', {'appel_offre_list': item_list, 'page_slug': 'appels-offre/', 'page_title': 'Appels offres'}, context_instance = RequestContext(request))

def appel_offre_detail(request, slug):
    p = get_object_or_404(Appel_Offre, slug=slug)

    return render_to_response('appel_offre_detail.html', {'appel_offre': p, 'page_slug': 'appels-offre/', 'page_title': 'Appels offres'}, context_instance = RequestContext(request))
