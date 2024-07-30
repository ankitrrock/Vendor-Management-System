"""
URL configuration for vender_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import (
    create_vendor, list_vendors, vendor_detail, update_vendor, delete_vendor,
    create_purchase_order, list_purchase_orders, purchase_order_detail, update_purchase_order, delete_purchase_order,
    vendor_performance
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/vendors/", list_vendors, name="list_vendors"),
    path("api/vendors/create/", create_vendor, name="create_vendor"),
    path("api/vendors/<int:vendor_id>/", vendor_detail, name="vendor_detail"),
    path("api/vendors/<int:vendor_id>/update/", update_vendor, name="update_vendor"),
    path("api/vendors/<int:vendor_id>/delete/", delete_vendor, name="delete_vendor"),
    path("api/purchase_orders/", list_purchase_orders, name="list_purchase_orders"),
    path("api/purchase_orders/create/", create_purchase_order, name="create_purchase_order"),
    path("api/purchase_orders/<int:po_id>/", purchase_order_detail, name="purchase_order_detail"),
    path("api/purchase_orders/<int:po_id>/update/", update_purchase_order, name="update_purchase_order"),
    path("api/purchase_orders/<int:po_id>/delete/", delete_purchase_order, name="delete_purchase_order"),
    path("api/vendors/<int:vendor_id>/performance/", vendor_performance, name="vendor_performance"),
]
