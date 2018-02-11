from django.urls import path, re_path
from . import views

app_name = 'whisky'

urlpatterns = [    
    path('search/', views.Search),
    re_path(r'search/(?P<query>\w+)', views.Search),
    path('create/', views.CreateWhisky),
]