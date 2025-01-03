from django.urls import path
from . import views

urlpatterns = [
    path('', views.xizmatlar_royxati, name='xizmatlar_royxati'),
    path('xizmat/<int:pk>/', views.xizmat_detail, name='xizmat_detail'),
    path('qidirish/', views.xizmat_qidirish, name='xizmat_qidirish'),
    path('xizmat/yangi/', views.xizmat_yaratish, name='xizmat_yaratish'),
    path('xizmat/<int:pk>/tahrirlash/', views.xizmat_tahrirlash, name='xizmat_tahrirlash'),
    path('xizmat/<int:pk>/ochirish/', views.xizmat_ochirish, name='xizmat_ochirish'),
]