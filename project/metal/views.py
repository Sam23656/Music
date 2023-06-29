from django.shortcuts import render
from metal.models import Metal


# Create your views here.


def show_metal_page(request):
    return render(request, "category.html", context={'objects': Metal.objects.all()})


def show_metal_profile_page(request, id):
    return render(request, "profile.html", context={'objects': Metal.objects.get(pk=id)})
