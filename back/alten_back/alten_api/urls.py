from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_post_products, name="get_post_products") ,
    path("<int:pk>", views.get_patch_delete_product, name="get_patch_delete_product")
]