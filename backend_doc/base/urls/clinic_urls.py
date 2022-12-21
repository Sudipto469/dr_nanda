from django.urls import path
from ..views import clinic_view as views

urlpatterns = [
    path("", views.getClinics, name="clinics"),
    # path("products/", views.getProducts, name="products"),
    # path("sort/",views.getSort, name = 'SortProduct'),
    # path("<str:pk>/", views.getProduct, name="product"),
    # path("<str:pk>/reviews/", views.createProductReview, name="product"),

]
