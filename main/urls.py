from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecordsView.as_view(),name="records"),
    path('record_control/',views.RecordsControlView.as_view(),name="record_control"),
    path('catalog_control/',views.CatalogControlView.as_view(),name="catalog_control"),
    path('catalog_control/type/<int:id>/edit/',views.TypeEditView.as_view(),name="type_edit"),
    path('catalog_control/type/<int:id>/delete/',views.TypeDeleteView.as_view(),name="type_delete"),
    path('catalog_control/category/<int:id>/edit/',views.CategoryEditView.as_view(),name="category_edit"),
    path('catalog_control/category/<int:id>/delete/',views.CategoryDeleteView.as_view(),name="category_delete"),
    path('catalog_control/subcategory/<int:id>/edit/',views.SubcategoryEditView.as_view(),name="subcategory_edit"),
    path('catalog_control/subcategory/<int:id>/delete/',views.SubcategoryDeleteView.as_view(),name="subcategory_delete"),
]