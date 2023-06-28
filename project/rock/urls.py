from django.urls import path
from rock.views import show_rock_page, show_rock_profile_page

urlpatterns = [
    path('', show_rock_page),
    path('<int:id>', show_rock_profile_page),
]
