from django.urls import path
from ..views import product_views as views

urlpatterns = [
    path("", views.getProducts, name="products"),
    path("sort/",views.getSort, name = 'SortProduct'),
    path("<str:pk>/", views.getProduct, name="product"),
    path("<str:pk>/reviews/", views.createProductReview, name="product"),

]
