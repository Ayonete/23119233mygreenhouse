from django.urls import path
# this imports all the views from the views.py
from . import views

urlpatterns = [
    # this is the home url
    path('', views.home, name='home'),
    # this is the single crop url
    path('crop-detail/<str:id>/', views.crop_detail, name='crop-detail'),
    # this is the add crop url
    path('add-crop/', views.add_crop, name='add-crop'),
    # this is the edit crop url
    path('edit-crop/<str:id>/', views.edit_crop, name='edit-crop'),
    # this is the delete crop url
    path('delete-crop/<str:id>/', views.delete_crop, name='delete-crop'),
    #this is for the diagnostics
    path('diagnostics/', views.diagnostics, name='diagnostics'),
]