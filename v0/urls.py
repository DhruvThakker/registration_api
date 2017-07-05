from django.conf.urls import url, include
import views
from rest_framework.routers import DefaultRouter

user_router = DefaultRouter()
user_router.register(r'register', views.UserViewSet)



urlpatterns = [


    url(r'^', include(user_router.urls)),
]
