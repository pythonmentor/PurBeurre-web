from django.urls import path

from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('legal-notice/', views.LegalNotice.as_view(), name='legal-notice'),
    path('alt-prod/', views.AlternativeProducts.as_view(), name='alt-prod'),
    path('prod-details/<pk>/', views.ProductDetail.as_view(), name='prod-details'),
    path('api/get_products/', views.get_products, name='get_products'),
]
