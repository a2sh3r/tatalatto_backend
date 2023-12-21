from django.urls import path

from products.views import ProductsView

app_name = 'products'

urlpatterns = [
    path("", ProductsView.as_view(), name="product-view"),

]