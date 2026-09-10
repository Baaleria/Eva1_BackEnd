from django.urls import path
from . import views

app_name = 'AppAndrea'

urlpatterns =[
    path('a1/', views.vista_Andrea, name = 'AppAndrea'),
    path('a2/', views.vista2_Andrea, name = 'AppAndrea2')
]