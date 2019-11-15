from django.shortcuts import render

# Create your views here.
from django.views import generic
from javbus.models import Movies
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from helpers import get_page_list


class IndexView(generic.ListView):
    model = Movies
    template_name = 'javbus/index.html'
    context_object_name = 'movie_list'
    paginate_by = 30
    c = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        page_list = get_page_list(paginator, page)
        context['c'] = self.c
        context['page_list'] = page_list
        return context

    def get_queryset(self):
        movie_list = Movies.objects.all().order_by('-release')
        return movie_list

class ModelDetailView(generic.DetailView):
    model = Movies
    template_name = "javbus/detail.html"
    context_object_name = "movie_obj"
    pk_url_kwarg = 'avnum'
    def get_object(self, queryset=None):
        avnum = self.kwargs.get(self.pk_url_kwarg)
        movie_obj = Movies.objects.get(avnum=avnum)
        return movie_obj
