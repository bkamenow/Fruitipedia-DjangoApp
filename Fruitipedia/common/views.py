from django.shortcuts import render

from helper.helper import get_profile, get_fruits


# Create your views here.


def home_page(request):
    profile = get_profile()

    context = {
        'profile': profile,
        }

    return render(request, template_name='common/index.html', context=context)


def dashboard(request):
    profile = get_profile()
    fruits = get_fruits()

    context = {
        'profile': profile,
        'fruits': fruits
    }

    return render(request, template_name='common/dashboard.html', context=context)
