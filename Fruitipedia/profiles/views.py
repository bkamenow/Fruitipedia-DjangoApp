from django.shortcuts import render, redirect

from Fruitipedia.fruits.forms import DeleteFruitForm
from Fruitipedia.profiles.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from helper.helper import get_profile, get_fruits


# Create your views here.


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form
    }

    return render(request, template_name='profile/create-profile.html', context=context)


def profile_details(request):
    profile = get_profile()
    fruits = get_fruits()

    total_posts = len(fruits)

    context = {
        'profile': profile,
        'total_posts': total_posts,
    }
    return render(request, template_name='profile/details-profile.html', context=context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, template_name='profile/edit-profile.html', context=context)


def delete_profile(request):
    profile = get_profile()
    fruits = get_fruits()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        form.save()
        for fruit in fruits:
            fruit_form = DeleteFruitForm(request.POST, instance=fruit)
            fruit_form.save()

        return redirect('home-page')

    context = {
        'profile': profile
    }

    return render(request, template_name='profile/delete-profile.html', context=context)
