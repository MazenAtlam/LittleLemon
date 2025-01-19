from django.urls import path
from . import views

urlpatterns = [
    path("menu-items", views.MenuItemListView.as_view(), name="menu-item-list"),
    path("categories", views.CategoryView.as_view(), name="menu-item-category"),
    path(
        "menu-items/<int:pk>",
        views.MenuItemDetailView.as_view(),
        name="menu-item-detail",
    ),
    path("groups/manager/users", views.ManagersListView.as_view(), name="manager-list"),
    path(
        "groups/managers/users/<int:pk>",
        views.ManagersRemoveView.as_view(),
        name="manager-remove",
    ),
    path(
        "groups/delivery-crew/users",
        views.DeliveryCrewListView.as_view(),
        name="delivery-crew-list",
    ),
    path(
        "groups/delivery-crew/users/<int:pk>",
        views.DeliveryCrewRemoveView.as_view(),
        name="delivery-crew-remove",
    ),
    path("cart/menu-items", views.CartOperationsView.as_view(), name="cart-operations"),
    path("cart/orders", views.OrderOperationsView.as_view(), name="order-operations"),
    path("orders/<int:pk>", views.SingleOrderView.as_view(), name="single-order"),
]
