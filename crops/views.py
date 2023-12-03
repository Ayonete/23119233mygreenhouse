from django.shortcuts import render
from django.http import HttpResponse

# this is a view for listing all the crops
def home(request):
    return HttpResponse('Home Page')

# this is a view for listing a single crop,it will take id as an argument
def crop_detail(request, id):
    return HttpResponse('crop Detail')

# this is a list for adding a crop
def add_crop(request):
    return HttpResponse('Add crop')

# this is a view for editing the crop's info
def edit_crop(request, id):
    return HttpResponse('Edit crop')
    
# this is a view for deleting a crop,it will take id as an argument
def delete_crop(request, id):
    return HttpResponse('Delete crop')
