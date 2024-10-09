from django.shortcuts import render


def start(request):
    return render(request, 'start.html')


def base(request, menu_name, active=None):
    context = {
        'menu_name': menu_name,
        'active': active
        }
    return render(request, 'base.html', context=context)
