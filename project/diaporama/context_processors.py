from diaporama.models import Slider
from django.template import Context, RequestContext
import datetime


def list_slider(request):
    list = Slider.objects.filter(status=3)
    return {
        'slider_list' : list
    }