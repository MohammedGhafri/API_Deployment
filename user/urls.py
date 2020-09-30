from django.urls import path
from .views import Authlist,Authdetails


urlpatterns = [
    path('', Authlist.as_view(), name='auth'), # localhost:8000/api/v1/posts
    path('<int:pk>/', Authdetails.as_view(), name='auth_details') # localhost:8000/api/v1/posts/1
]