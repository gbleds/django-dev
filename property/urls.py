from django.urls import path, re_path

from .views import (
	PropertyListView,
	PropertyDetailView,
	PropertyCreateView,
	PropertyUpdateView,
	SearchResultsView
)

urlpatterns = [
    re_path(r'^$', PropertyListView.as_view(), name='list'),
    re_path(r'^create/$', PropertyCreateView.as_view(), name='create'),
    re_path(r'^(?P<pk>[\d-]+)/$', PropertyDetailView.as_view(), name="detail"), 
	path('search/', SearchResultsView.as_view(), name='search_results'),
]