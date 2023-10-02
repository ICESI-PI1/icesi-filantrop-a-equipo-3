from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.models import Donor
from MSDE_App.forms import CreateDonor


def create_donor(request):
    if request.method == 'POST':
        try:
            form = CreateDonor(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        except ValueError:
            return render(request, 'donor/create_donor.html', {
                'form': form,
                'error': 'Please provide valid data'
            })
    else:
        form = CreateDonor()
    return render(request, 'donor/create_donor.html', {'form': form})


def donor_detail(request, donor_code):
    donor = get_object_or_404(Donor, donor_code=donor_code)
    return render(request, 'donor/donor_detail.html', {
        'donor': donor
    })


def donor_view(request):
    donor_list = Donor.objects.all()
    return render(request, 'donor/donors.html', {
        'donors': donor_list
    })


def edit_donor(request, donor_code):
    donor = get_object_or_404(Donor, donor_code=donor_code)
    if request.method == 'POST':
        form = CreateDonor(request.POST, instance=donor)
        if form.is_valid():
            form.save()
    else:
        form = CreateDonor(instance=donor)
    return render(request, 'donor/edit_donor.html', {'form': form, 'donor': donor})


def delete_donor(request, donor_code):
    donor = get_object_or_404(Donor, donor_code=donor_code)
    if request.method == 'POST':
        donor.delete()
        return redirect('donors/')
    return render(request, 'donor/delete_donor.html', {'donor': donor})