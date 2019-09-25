from django.shortcuts import render
from accounts.models import User
from django.views.generic.detail import DetailView

class UserDetailView(DetailView):
    queryset = User.objects.all()