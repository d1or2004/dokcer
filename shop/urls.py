from django.urls import path
from .views import LandingView, ShopView, ShopDetailView, AddToCartView, ProductDetailView, CartView, ContactView, ProductListView

urlpatterns = [
    path('shop/', LandingView.as_view(), name='landing-shop'),
    path('shop_shop/', ShopView.as_view(), name='shop'),
    path('shop_detail/', ShopDetailView.as_view(), name='shop-detail'),
    path('add_to_cart/<int:id>/', AddToCartView.as_view(), name='add-to-cart'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='shop-detail'),
    path('cart/', CartView.as_view(), name='card'),
    path('contact_view/', ContactView.as_view(), name='contact'),
    path('detail/', ProductListView.as_view(), name='product-list'),

]
