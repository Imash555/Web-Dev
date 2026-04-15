from django.urls import path

from .views import (
    CategoryDetailAPIView,
    CategoryListAPIView,
    CategoryProductsAPIView,
    ProductDetailAPIView,
    ProductListAPIView,
)


urlpatterns = [
    path("categories/", CategoryListAPIView.as_view(), name="category-list-create"),
    path("categories/<int:category_id>/", CategoryDetailAPIView.as_view(), name="category-rud"),
    path(
        "categories/<int:category_id>/products/",
        CategoryProductsAPIView.as_view(),
        name="category-products-list",
    ),
    path("products/", ProductListAPIView.as_view(), name="product-list-create"),
    path("products/<int:product_id>/", ProductDetailAPIView.as_view(), name="product-rud"),
]