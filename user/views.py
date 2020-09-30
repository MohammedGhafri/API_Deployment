from django.shortcuts import render
from rest_framework import generics
from .models import Auth
# Create your views here.
from .serializer import AuthSerializer
# from .permissions import IsAutherorReadOnly
from .permissions import IsAuthorOrReadOnly

class Authlist(generics.ListCreateAPIView):
    queryset = Auth.objects.all()
    serializer_class = AuthSerializer

class Authdetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthorOrReadOnly,)
    queryset = Auth.objects.all()
    serializer_class = AuthSerializer


