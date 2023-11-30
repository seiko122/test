from django.shortcuts import render
from .serializers import RegisterSerializer ,ProfileSerializers ,ProductSerializers ,ImageSerializers
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Profile , Images ,Product

from rest_framework.permissions import AllowAny , IsAdminUser,IsAuthenticated

class ProductsView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [IsAuthenticated]
    filterset_fields = ('is_sale','status')
class ProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [IsAuthenticated]
    filterset_fields = ('is_sale','status')
class ProductAdmin(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [IsAdminUser]
    filterset_fields = ('is_sale','status')
class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [IsAdminUser]
    filterset_fields = ('is_sale','status')

class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    
class ImageView(generics.ListAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializers
    permission_classes = [AllowAny]

class ImageViewAdmin(generics.RetrieveUpdateDestroyAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializers
    permission_classes = [IsAdminUser]
class ImageCreate(generics.CreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializers
    permission_classes = [IsAdminUser]

class ProfileView(generics.RetrieveUpdateDestroyAPIView,):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
    def get_object(self):
        queryset = Profile.objects.get(user=self.request.user)
        return queryset