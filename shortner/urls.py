from django.urls import path
from .views import index, retrieve

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('<str:pk>', retrieve.as_view(), name='retrieve')
]