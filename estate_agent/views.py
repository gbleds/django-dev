from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .forms import EstateAgentCreateForm, EstateAgentCreateFormModel
from .models import EstateAgent
from property.models import Property

@login_required(login_url='login.html')
def estate_agent_createview(request):
	form = EstateAgentCreateFormModel(request.POST or None)
	errors = None
	if form.is_valid():
		if request.user.is_authenticated():
			instance = form.save(commit=False)
			instance.owner = request.user
			instance.save()
			return HttpResponseRedirect("/estate_agents/")
		else:
			return HttpResponseRedirect("/login/")
	
	if form.errors:
		print(form.errors)
		errors = form.errors

	template_name = 'estate_agent/form.html'
	context = {"form": form, "errors": errors}
	return render(request, template_name, context)

class HomeView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, *args, **kwargs):
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		mylist = [1, 2, 3, 4, 6]
		context ={
			"name": "Bledi",
			"age": 24,
			"mylist": mylist
		}

		print (context)
		return context

class EstateAgentListView(ListView):
	queryset = EstateAgent.objects.all()
	template_name='estate_agent/estate_agent_list.html'

	def get_queryset(self):
		print (self.kwargs)
		slug = self.kwargs.get("slug")
		if slug:
			queryset = EstateAgent.objects.filter(
				Q(address2__iexact=slug) |
				Q(address2__icontains=slug)
			)
		else:			
			queryset = EstateAgent.objects.all()
		return queryset

class EstateAgentDetailView(DetailView):
	queryset = EstateAgent.objects.all()
	# property_queryset = Property.objects.filter(estate_agent=self.kwargs['estate_agent'])

class EstateAgentCreateView(LoginRequiredMixin, CreateView):
	form_class = EstateAgentCreateFormModel
	template_name = 'form.html'
	# success_url = "/estate_agents/"
	login_url="/login/"

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		# instance.save()
		return super(EstateAgentCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(EstateAgentCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Estate Agent'
		return context