from django.urls import path
from . import views

app_name = 'AppValeria'

urlpatterns = [
    path('va1/', views.vista_AppValeria, name ='AppValeria1'),
    path('va1/', views.vista_AppValeria, name ='AppValeria2')
]