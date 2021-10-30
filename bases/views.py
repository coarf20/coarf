from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy


from django.contrib.auth.mixins import LoginRequiredMixin,\
    PermissionRequiredMixin
from django.views import generic

from .models import Idioma,Frase


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url='bases:login'
    

class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    login_url = "bases:login"
    template_name="bases/sin_privilegios.html"

    
class IdiomaList(generic.ListView):
    template_name = "bases/idiomas.html"
    model = Idioma
    context_object_name="obj"