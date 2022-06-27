from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'usuario/usuario_crear_cuenta_form.html'
  success_url = reverse_lazy('blogs_iniciarsesion')
  form_class = UserCreationForm
  success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"

class BloggerProfile(DetailView):

    model = User
    template_name = "usuario/usuario_detalle.html"


class BloggerUpdate(LoginRequiredMixin, UpdateView):

    model = User
    template_name = "usuario/usuario_form.html"
    fields = ["username", "email", "first_name", "last_name"]

    def get_success_url(self):
      return reverse_lazy("usuario_perfil", kwargs={"pk": self.request.user.id})

class BlogLogin(LoginView):
    template_name = 'blogs/blogs_iniciarsesion.html'
    next_page = reverse_lazy("blogs_listas") 