from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/', view=views.product_list),
]