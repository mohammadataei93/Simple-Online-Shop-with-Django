from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('crate/', views.OrderCreateView.as_view(), name='order-create'),
    path('detail/<int:order_id>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/add/<int:product_id>/', views.CartAddView.as_view(), name='cart-add'),
    path('cart/remove/<int:product_id>/', views.CartRemoveView.as_view(), name='cart-remove'),
    path('apply/<int:order_id>/' , views.ApplyCouponView.as_view(), name='apply-coupon')
]