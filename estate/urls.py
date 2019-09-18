"""estate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView

from django.contrib.auth.views import LoginView

from estate_agent.views import (
    HomeView, 
    EstateAgentListView,
    EstateAgentDetailView, 
    EstateAgentCreateView,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^estate_agent/', include(('estate_agent.urls', 'estate_agents'), namespace='estate_agents')),
    url(r'^property/', include(('property.urls', 'property'), namespace='property')),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html"), name='contact'),
]
