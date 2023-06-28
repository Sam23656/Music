from django.urls import path
from pop.views import show_pop_page, show_pop_profile_page

urlpatterns = [
    path('', show_pop_page),
    path('<int:id>', show_pop_profile_page),
]
