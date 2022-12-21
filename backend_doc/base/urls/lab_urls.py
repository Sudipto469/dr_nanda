from django.urls import path
from ..views import lab_view as views

urlpatterns = [
    path("", views.getLabs, name="labs"),
    # path("products/", views.getProducts, name="products"),
    # path("sort/",views.getSort, name = 'SortProduct'),
    # path("<str:pk>/", views.getProduct, name="product"),
    # path("<str:pk>/reviews/", views.createProductReview, name="product"),

]
