from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset') #register viewsets with the router
router.register('profile', views.UserProfileViewSet) #base_name not required as base_name will be auto assigned to the name in the queryset (you could override it if you wanted by specifying it)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]