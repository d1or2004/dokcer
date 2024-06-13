from django.urls import path, include
from .views import LandingAPIView, MasterChefCreateAPIView, MasterChefUpdateAPIView, MasterChefDeleteAPIView, \
    ProductTypeSetAPIView, FoodMenuSetAPIView, TableOnlineSetAPIView, ContactSetAPIView, CostumerSetAPIView, \
    TestimonialSetAPIView, ServiceSetAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductTypeSetAPIView)
router.register('food', FoodMenuSetAPIView)
router.register('table', TableOnlineSetAPIView)
router.register('contact', ContactSetAPIView)
router.register('costumer', CostumerSetAPIView)
router.register('testimonial', TestimonialSetAPIView)
router.register('service', ServiceSetAPIView)

urlpatterns = [
    path('', LandingAPIView.as_view(), name='landing-api'),
    path('chef/create/', MasterChefCreateAPIView.as_view(), name='chef-create'),
    path('chef/<int:id>/update/', MasterChefUpdateAPIView.as_view(), name='chef-update'),
    path('', include(router.urls)),
    path('chef/<int:id>/delete/', MasterChefDeleteAPIView.as_view(), name='chef-delete'),

]
