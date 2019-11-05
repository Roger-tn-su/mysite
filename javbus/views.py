from django.shortcuts import render

# Create your views here.
from django.views import generic
from javbus.models import Movies
from django.http import HttpResponse
from django.template import loader

class IndexView(generic.ListView):
    model = Movies
    template_name = 'javbus/index.html'
    context_object_name = 'javbus_list'
    paginate_by = 6
    c = None
