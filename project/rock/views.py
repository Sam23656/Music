from django.shortcuts import render
from rock.models import Rock


# Create your views here.


def show_rock_page(request):
    return render(request, "category.html", context={'rock_objects': Rock.objects.all()})


def show_rock_profile_page(request, id):
    return render(request, "profile.html", context={'rock_objects': Rock.objects.get(pk=id)})
