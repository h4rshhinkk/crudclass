from django.shortcuts import render
from .models  import Core
from django.views.generic import ListView, DetailView,CreateView, TemplateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class IndexView(ListView):
    model = Core
    template_name = 'web/index.html'
    context_object_name = 'blog'


class SingleView(DetailView):
    model= Core
    template_name = 'web/single.html'
    context_object_name = 'post'


class PostView(ListView):
    model = Core
    template_name = 'web/posts.html'
    context_object_name = 'post_list'


class AddView(CreateView):
    model = Core
    
    template_name = 'web/add.html'
    fields = '__all__'
    success_url = reverse_lazy('web:posts')
    
class EditView(UpdateView):
    model = Core
    template_name = 'web/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('web:posts')

class Delete(DeleteView):
    model = Core
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('web:posts')
    template_name = 'web/confirm-delete.html'
