# -*- encoding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import Context, RequestContext
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from photos.models import *

def album(request):
    item_list = Album.objects.filter(actif=True).order_by('-date_album')
    return render_to_response('album.html', {'album_list': item_list, 'page_slug': 'album/', 'page_title': 'Album'}, context_instance = RequestContext(request))
    
def album_detail(request, id):
    album_detail = Album.objects.get(id=id)
    list_photo = Photo.objects.filter(album=id)
    return render_to_response('photos.html', {'album_detail': album_detail, 'list_photo': list_photo}, context_instance = RequestContext(request))