
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy

from cats.models import Cat,Breed

# Create your views here.

class CatList(LoginRequiredMixin,View):
    def get(self,request):
        cats = Cat.objects.all()
        bc = Breed.objects.all().count()

        ctx = {'breed_count':bc,'cat_list':cats}
        return render(request,'cats/cat_list.html', ctx)

class BreedList(LoginRequiredMixin,View):
    def get(self,request):
        breeds = Breed.objects.all()
        ctx = {'breed_list': breeds}
        return render(request,'cats/breed_list.html', ctx)

class BreedCreate(LoginRequiredMixin,CreateView):
    model = Breed
    fields = '__all__'
    success_url= reverse_lazy('cats:all')

class BreedUpdate(LoginRequiredMixin,UpdateView):
    model = Breed
    fields='__all__'
    success_url= reverse_lazy('cats:all')

class BreedDelete(LoginRequiredMixin,DeleteView):
    model = Breed
    fields='__all__'
    success_url= reverse_lazy('cats:all')


class CatCreate(LoginRequiredMixin,CreateView):
    model = Cat
    fields = '__all__'
    success_url= reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin,UpdateView):
    model = Cat
    fields='__all__'
    success_url= reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin,DeleteView):
    model = Cat
    fields='__all__'
    success_url= reverse_lazy('cats:all')

