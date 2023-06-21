from django.urls import path
from jazz.views import show_jazz_page, show_jazz_profile_page

urlpatterns = [
    path('', show_jazz_page),
    path('<int:id>', show_jazz_profile_page),
]
