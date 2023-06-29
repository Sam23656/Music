from django.shortcuts import render
from pop.models import Pop


# Create your views here.


def show_pop_page(request):
    return render(request, "category.html", context={'objects': Pop.objects.all()})


def show_pop_profile_page(request, id):
    return render(request, "profile.html", context={'objects': Pop.objects.get(pk=id)})
