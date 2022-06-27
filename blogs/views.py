from ast import Index
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from blogs.models import BlogModel, BlogModel2 
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogList(LoginRequiredMixin, ListView):
    login_url = '/usuario/entrar/'
    model = BlogModel
    model2 = User
    template_name = "blogs/blogs_listas.html"   



class BlogDetail(DetailView):

    model = BlogModel
    template_name = "blogs/blogs_detalles.html"


class BlogCreate(LoginRequiredMixin, CreateView):

    model = BlogModel
    success_url = reverse_lazy("blogs_listas")
    fields = ["titulo", "sub_titulo", "cuerpo"]
    readonly_fields = ['created', "fecha_creacion"]

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class BlogUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = BlogModel
    success_url = reverse_lazy("blogs_listas")
    fields = ["titulo", "sub_titulo", "cuerpo" ]
    readonly_fields = ["fecha_creacion"]

    def test_func(self):
        exist = BlogModel.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False








class BlogList2(LoginRequiredMixin, ListView):
    login_url = '/usuario/entrar/'
    model = BlogModel2
    template_name = "blogs/blogmodel2_list.html"          

class BlogCreate2(LoginRequiredMixin, CreateView):

    model = BlogModel2
    success_url = reverse_lazy("blogs_listas2")
    fields = ["profesor", "materia", "tarea"]
    readonly_fields = ['created', "fecha_creacion2"]

    def form_valid(self, form):
        form.instance.autor2 = self.request.user
        return super().form_valid(form)

        
class BlogUpdate2(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = BlogModel2
    success_url = reverse_lazy("blogs_listas2")
    fields = ["profesor", "materia", "tarea" ]
    readonly_fields = ["fecha_creacion2"]

    def test_func(self):
        exist = BlogModel2.objects.filter(autor2=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False



class BlogDelete2(LoginRequiredMixin,UserPassesTestMixin, DeleteView):

    model = BlogModel2
    success_url = reverse_lazy("blogs_listas2")

    def test_func(self):
        exist = BlogModel2.objects.filter(autor2=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False



class BlogDetail2(DetailView):

    model = BlogModel2
    template_name = "blogs/blogs_detalles2.html"











        

class BlogDelete(LoginRequiredMixin,UserPassesTestMixin, DeleteView):

    model = BlogModel
    success_url = reverse_lazy("blogs_listas")

    def test_func(self):
        exist = BlogModel.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False


class BlogLogin(LoginView):
    template_name = 'blogs/blogs_iniciarsesion.html'
    next_page = reverse_lazy("blogs_listas")


class BlogLogout(LoginRequiredMixin, LogoutView):
    template_name = 'blogs/blogs_desconectar.html'
    

class About(LoginRequiredMixin, ListView):
    login_url = '/usuario/entrar/'
    model = BlogModel
    template_name = "blogs/about.html"

class Index(ListView):
    model = BlogModel
    template_name = 'blogs/index.html'