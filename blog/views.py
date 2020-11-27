from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from . models import Post
from django.urls import reverse_lazy
# Create your views here.

class BlogListView(ListView): # Listagem dos posts
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView(DetailView): # Detalhamento dos posts
	model = Post
	template_name = 'blog/post_detail.html'
	#context_object_name = 'custom'
	
class BlogCreateView(CreateView): # Criação dos posts
	model = Post
	template_name = 'blog/post_new.html'
	fields = 'titulo','autor','conteudo','status'
	
class BlogUpdateView(UpdateView): # Edição dos posts
	model = Post
	template_name = 'blog/post_edit.html'
	fields = 'titulo','conteudo'
	success_url = reverse_lazy('post_detail')
	
class BlogDeleteView(DeleteView): # Edição dos posts
	model = Post
	template_name = 'blog/post_delete.html'
	fields = 'titulo','conteudo'
	success_url = reverse_lazy('home')