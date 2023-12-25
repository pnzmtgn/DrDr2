from django.urls import path
from .views import List_SPC, List_html

urlpatterns = [
    path('', List_html),
    path('<str:speciality_name/>', List_SPC)
]

