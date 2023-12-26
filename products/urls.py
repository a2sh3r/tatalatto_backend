from django.conf.urls.static import static
from django.urls import path

from products.views import ProductsListView, CakesListView, CupcakesListView, TriflesListView, GingersListView, \
    MarshmallowsListView, CakesDetailView, CupcakesDetailView, GingersDetailView, TriflesDetailView, \
    MarshmallowsDetailView
from tatalatto_backend import settings

app_name = 'products'

urlpatterns = [
    path("", ProductsListView.as_view(), name="product-view"),
    path("cakes", CakesListView.as_view(), name="cake-view"),
    path("cakes/<int:pk>", CakesDetailView.as_view(), name="cake-detail-view"),
    path("cupcakes", CupcakesListView.as_view(), name="cupcake-view"),
    path("cupcakes/<int:pk>", CupcakesDetailView.as_view(), name="cupcake-detail-view"),
    path("gingers", GingersListView.as_view(), name="ginger-view"),
    path("gingers/<int:pk>", GingersDetailView.as_view(), name="ginger-detail-view"),
    path("trifles", TriflesListView.as_view(), name="trifle-view"),
    path("trifles/<int:pk>", TriflesDetailView.as_view(), name="trifle-detail-view"),
    path("marshmallows", MarshmallowsListView.as_view(), name="marshmallow-view"),
    path("marshmallows/<int:pk>", MarshmallowsDetailView.as_view(), name="marshmallow-detail-view"),
]
