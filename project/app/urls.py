from django.urls import path
from .views import index,category,product
urlpatterns = [
    path('', index),
    path('product/',product),
    path('category/', category),
    path('category/<int:id>/',category),
    path('category/<slug:category_slug>/',category),
]
