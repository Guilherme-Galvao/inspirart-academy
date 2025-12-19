from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import CourseViewSet # Will be uncommented when views are created

router = DefaultRouter()
# router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
