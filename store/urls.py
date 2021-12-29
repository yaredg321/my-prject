from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store,name = 'store'),
    path('cart/', views.cart,name = 'cart'),
    path('checkout/', views.checkout,name = 'checkout'),
    path('up_login/', views.up_login,name = 'up_login'),
    path('register/', views.register,name = 'register'),
    path('detail/<int:id>/', views.detail, name="detail"),
    path('add-to-cart/<int:id>/', views.add_to_cart),
    path('upload/', views.upload, name='upload')
]