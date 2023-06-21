from django.shortcuts import render
from category.models import Categorys


# Create your views here.


def show_index_page(request):
    return render(request, "index.html", context={"Categorys": Categorys.objects.all()})
