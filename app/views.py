import imp
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import *
from .forms import *
# Create your views here.
@require_http_methods(["GET", "POST"])
def home(request: HttpRequest) -> HttpResponse:
    qs = vlanModel.objects.all()
    context = {'datos': qs}
    return render(request,"home.html",context)

@require_http_methods(["POST",])
def agregarVlan(request: HttpRequest) -> HttpResponse:
    form = vlanForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = vlanForm(request.POST)
    context = {'form': form}
    return render(request,"home.html",context)
