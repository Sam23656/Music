from django.shortcuts import render
from jazz.models import Jazz


# Create your views here.


def show_jazz_page(request):
    return render(request, "category.html", context={'objects': Jazz.objects.all()})


def show_jazz_profile_page(request, id):
    return render(request, "profile.html", context={'objects': Jazz.objects.get(pk=id)})
