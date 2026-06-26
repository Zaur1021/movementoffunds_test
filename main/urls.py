from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecordsView.as_view(),name="records"),
    path('record_control/',views.RecordsControlView.as_view(),name="record_control"),
    path('catalog_control/',views.CatalogControlView.as_view(),name="catalog_control")
]