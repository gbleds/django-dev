from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Property
from .forms import PropertyForm
# Create your views here.

class PropertyListView(ListView):
	def get_queryset(self):
		return Property.objects.filter(user=self.request.user)

class PropertyDetailView(DetailView):
	def get_queryset(self):
		return Property.objects.filter(user=self.request.user)

class PropertyCreateView(CreateView):
	form_class = PropertyForm
	def get_queryset(self):
		return Property.objects.filter(user=self.request.user)

class PropertyUpdateView(UpdateView):
	form_class = PropertyForm
	def get_queryset(self):
		return Property.objects.filter(user=self.request.user)