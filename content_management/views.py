from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import EducationalMaterial
from .forms import EducationalMaterialForm

def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def add_material(request):
    if request.method == 'POST':
        form = EducationalMaterialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Material successfully added.')
            return redirect('material_list')
        else:
            messages.error(request, 'There was an error adding the material.')
    else:
        form = EducationalMaterialForm()
    return render(request, 'content_management/add_material.html', {'form': form})

@user_passes_test(is_superuser)
def edit_material(request, pk):
    material = get_object_or_404(EducationalMaterial, pk=pk)
    if request.method == 'POST':
        form = EducationalMaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            messages.success(request, 'Material successfully updated.')
            return redirect('material_list')
        else:
            messages.error(request, 'There was an error updating the material.')
    else:
        form = EducationalMaterialForm(instance=material)
    return render(request, 'content_management/edit_material.html', {'form': form})

def material_list(request):
    materials = EducationalMaterial.objects.all()
    return render(request, 'content_management/material_list.html', {'materials': materials})
