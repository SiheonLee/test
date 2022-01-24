from django.urls import path, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# ADMIN EMAIL: admin@example.com USERNAME: admin PASSWORD: password123
# TODO
# We can even do a oneliner for simple views like the following!
# path('properties/', ListCreateAPIView.as_view(queryset=User.objects.all(), serializer_class=UserSerializer), name='user-list')

urlpatterns = [
    path('properties/', views.PropertyList.as_view()),
    path('properties/<str:externalId>/', views._property.as_view(), name='externalId'),
    path('city/<str:city>', views.City.as_view(), name='city')
    ]

urlpatterns = format_suffix_patterns(urlpatterns)