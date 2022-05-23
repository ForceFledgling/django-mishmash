from django.urls import path

from . import views


urlpatterns = [
    path(r'', views.list_pages_view, name='list_pages_view'),
    path('<str:page_id>/', views.page_view, name='page_view'),
    path('<str:page_id>/edit/', views.edit_page, name='edit_page'),
    path('<str:page_id>/save/', views.save_page, name='save_page'),
]
