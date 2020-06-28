from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from django.utils import timezone
from .models import Item
class HomeView(ListView):
    model=Item
    template_name="home.html"

class ItemDetailView(DetailView):
    model=Item
    template_name='product.html'
def checkout(request):
    return render(request,"checkout.html")

