from django.conf.urls import url

from .views import (
	PropertyListView,
	PropertyDetailView,
	PropertyCreateView,
	PropertyUpdateView
)

urlpatterns = [
    url(r'^$', PropertyListView.as_view(), name='list'),
    url(r'^create/$', PropertyCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', PropertyDetailView.as_view(), name="detail"), 
]