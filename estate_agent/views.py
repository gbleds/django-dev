from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from .models import EstateAgent

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


def estateagent_listview(request):
	template_name='estate_agent/estate_agent_list.html'
	queryset = EstateAgent.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)

class EstateAgentListView(ListView):
	queryset = EstateAgent.objects.all()
	template_name='estate_agent/estate_agent_list.html'


class ChelmsfordEstateAgentListView(ListView):
	queryset = EstateAgent.objects.filter()
	template_name='estate_agent/estate_agent_list.html'