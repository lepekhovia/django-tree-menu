from django.shortcuts import render


def base(request, url_path=None):
    return render(request, 'base.html')
