from django.urls import path, re_path

from .views import (
    UserDetailView, 
)

urlpatterns = [
    # re_path(r'^$', EstateAgentListView.as_view(), name='list'),
    # re_path(r'^create/$', EstateAgentCreateView.as_view(), name='create'),
    re_path(r'^(?P<pk>[\w-]+)/$', UserDetailView.as_view(), name="detail"), 
]
