from django.urls import path
from .views import home,login,signup,cart,checkout,orders
from .views.login import logout
urlpatterns = [
    path('',home.Index.as_view(), name="homepage"),
    path('signup', signup.Signup.as_view(),name='signup'),
    path('login',login.Login.as_view(),name='login'),
    path('logout',logout,name='logout'),
    path('cart',cart.Cart.as_view(),name="cart"),
    path('check-out', checkout.Checkout.as_view(),name='checkout'),
    path('orders', orders.OrderView.as_view(),name='orders')
]