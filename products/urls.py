from django.urls import path
# math url to function
from . import views
# . means current folder

# views.index()

# /products
# /products/1/detail
# /products/new
# /products/trending

urlpatterns = [
    path('', views.index),
    path('new/', views.new)
]


