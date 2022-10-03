from django.urls import path, include
from . import views

app_name = 'api'
urlpatterns = [
    path('', views.ApiListView.as_view(), name='list'),
    path('detail', views.ApiDetailView.as_view(), name='detail')
]
