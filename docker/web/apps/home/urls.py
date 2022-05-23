from django.urls import path

from .views import home_view

urlpatterns = [
    path(r'', home_view, name='home_view'),
]
