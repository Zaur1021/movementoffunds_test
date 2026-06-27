from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecordsView.as_view(),name="records"),
    path('record_control/',views.RecordsControlView.as_view(),name="record_control"),
    path('catalog_control/',views.CatalogControlView.as_view(),name="catalog_control"),
    path('catalog_control/type/<int:id>/',views.TypeEditView.as_view(),name="type_edit"),
    path('catalog_control/type/<int:id>/delete',views.TypeDeleteView.as_view(),name="type_delete"),
]