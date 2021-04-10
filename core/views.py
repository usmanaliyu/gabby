from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, View
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.utils import timezone
from django.urls import reverse_lazy, reverse

from django.core.paginator import Paginator






from .models import *

# Create your views here.

def HomeView(request):
    return render(request, 'index.html')