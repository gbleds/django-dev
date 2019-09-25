from django.conf.urls import url
from django.urls import path, re_path

from .views import (
    HomeView, 
    EstateAgentListView,
    EstateAgentDetailView, 
    EstateAgentCreateView,
)

urlpatterns = [
    re_path(r'^$', EstateAgentListView.as_view(), name='list'),
    re_path(r'^create/$', EstateAgentCreateView.as_view(), name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$', EstateAgentDetailView.as_view(), name="detail"), 
]
