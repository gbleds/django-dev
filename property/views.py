from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
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

class PropertyCreateView(LoginRequiredMixin, CreateView):
	template_name = 'form.html'
	form_class = PropertyForm

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		return super(PropertyCreateView, self).form_valid(form)

	def get_form_kwargs(self, *args, **kwargs):
		kwargs = super(PropertyCreateView, self).get_form_kwargs(*args, **kwargs)
		kwargs['user'] = self.request.user
		return kwargs	

	def get_queryset(self):
		return Property.objects.filter(user=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super(PropertyCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Create Property'
		return context

class PropertyUpdateView(LoginRequiredMixin, UpdateView):
	template_name = 'form.html'
	form_class = PropertyForm
	def get_queryset(self):
		return Property.objects.filter(user=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super(PropertyUpdateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Update Property'
		return context