from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def handler400(request):
    return render(request, '400.html', status=404)


def handler403(request):
    return render(request, '403.html', status=500)


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
