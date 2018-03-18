from django.conf.urls import url

from .views import (
    HomeView, 
    EstateAgentListView,
    EstateAgentDetailView, 
    EstateAgentCreateView,
)

urlpatterns = [
    url(r'^$', EstateAgentListView.as_view(), name='list'),
    url(r'^create/$', EstateAgentCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', EstateAgentDetailView.as_view(), name="detail"), 
]
