from django.urls import path
from .views import RegisterUser ,ProfileView ,ImageView ,ProductAdmin ,ProductCreate,ProductsView,ProductView ,ImageCreate,ImageViewAdmin



urlpatterns = [
    path('register/',RegisterUser.as_view()),
    path('profile/',ProfileView.as_view()),
    path('images/',ImageView.as_view()),
    path('images/<int:pk>',ImageViewAdmin.as_view()),
    path('images/create',ImageCreate.as_view()),
    path('products/',ProductsView.as_view()),
    path('products/create',ProductCreate.as_view()),
    path('products/<int:pk>',ProductView.as_view()),
    path('products/<int:pk>',ProductAdmin.as_view()),
]