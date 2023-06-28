from django.urls import path
from electronic.views import show_electronic_page, show_electronic_profile_page

urlpatterns = [
    path('', show_electronic_page),
    path('<int:id>', show_electronic_profile_page),
]
