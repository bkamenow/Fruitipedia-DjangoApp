from django.shortcuts import render, redirect

from Fruitipedia.fruits.forms import CreateFruitForm, EditFruitForm, DeleteFruitForm
from helper.helper import get_profile, get_fruit


# Create your views here.


def create_fruit(request):
    profile = get_profile()
    if request.method == 'GET':
        form = CreateFruitForm()
    else:
        form = CreateFruitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, template_name='fruit/create-fruit.html', context=context)


def fruit_details(request, pk):
    profile = get_profile()
    fruit = get_fruit(pk)

    context = {
        'profile': profile,
        'fruit': fruit,
    }
    return render(request, template_name='fruit/details-fruit.html', context=context)


def edit_fruit(request, pk):
    profile = get_profile()
    fruit = get_fruit(pk)

    if request.method == 'GET':
        form = EditFruitForm(instance=fruit)
    else:
        form = EditFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
        'fruit': fruit,
    }
    return render(request, template_name='fruit/edit-fruit.html', context=context)


def delete_fruit(request, pk):
    profile = get_profile()
    fruit = get_fruit(pk)

    if request.method == 'GET':
        form = DeleteFruitForm(instance=fruit)
    else:
        form = DeleteFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'fruit': fruit,
        'form': form,
    }
    return render(request, template_name='fruit/delete-fruit.html', context=context)
