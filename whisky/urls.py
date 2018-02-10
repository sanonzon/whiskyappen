from django.urls import path, re_path
from . import views

app_name = 'whisky'

urlpatterns = [    
    path('search/<slug:query>', views.Search)
]