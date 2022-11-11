from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

urlpatterns = [
    path("all", views.get_all_products, name="all"),
    path("<int:unique_code>", views.product, name="detail"),
]
urlpatterns+= router.urls
