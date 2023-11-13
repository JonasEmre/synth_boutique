from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:item_id>/', views.detail , name='details'),
]