from django.shortcuts import render
from electronic.models import Electronic


# Create your views here.


def show_electronic_page(request):
    return render(request, "category.html", context={'jazz_objects': Electronic.objects.all()})


def show_electronic_profile_page(request, id):
    return render(request, "profile.html", context={'jazz_objects': Electronic.objects.get(pk=id)})
