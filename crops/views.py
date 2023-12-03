from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Crop
from .forms import EditCropForm, DiagnosticsForm

# this is a view for listing all the crops
def home(request):
    crops = Crop.objects.all()
    context = {'crops': crops}
    return render(request, 'crops/home.html', context)

# this is a view for listing a single crop,it will take id as an argument
def crop_detail(request, id):
    crop = Crop.objects.get(pk=id)
    context = {'crop': crop}
    return render(request, 'crops/crop-detail.html', context)

# this is a list for adding a crop
def add_crop(request):
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image-file')
        
        crop = Crop.objects.create(
            name = data['name'],
            description = data['description'],
            temperature = data['temperature'],
            moisture = data['moisture'],
            image = image
            )
        return redirect('home')
    return render(request, 'crops/add-crop.html')

# this is a view for editing the crop's info
def edit_crop(request, id):
    crop = Crop.objects.get(pk=id)
    
    form = EditCropForm(instance=crop)
    
    if request.method == 'POST':
        form = EditCropForm(request.POST, request.FILES, instance=crop)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'crops/update-crop.html', context)
    
# this is a view for deleting a crop,it will take id as an argument
# this is a view for deleting a book
def delete_crop(request, id):
    # getting the book to be deleted
    crop = Crop.objects.get(pk=id)
    # checking if the method is POST
    if request.method == 'POST':
        # delete the book
        crop.delete()
        # return to home after a success delete
        return redirect('home')
    context = {'crop': crop}
    return render(request, 'crops/delete-crop.html', context)


def diagnostics(request):
    if request.method == 'POST':
        form = DiagnosticsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('While we work on making this page more dynamic, please check your email for the results of your diagnostic check. Happy Planting!')
    else:
        form = DiagnosticsForm()

    return render(request, 'crops/diagnostics.html', {'form': form})