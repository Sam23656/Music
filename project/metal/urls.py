from django.urls import path
from metal.views import show_metal_page, show_metal_profile_page

urlpatterns = [
    path('', show_metal_page),
    path('<int:id>', show_metal_profile_page),
]
