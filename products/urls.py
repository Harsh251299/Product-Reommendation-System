from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("params=<str:param>", views.params, name="params"),
    path("name",views.name,name="name"),
    path("filterSelect",views.filterSelect,name="filterSelect"),
    path("namepage",views.nextPage,name="nextpage"),
    path("previouspage",views.previousPage,name="previouspage")
]