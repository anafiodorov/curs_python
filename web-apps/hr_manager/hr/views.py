from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage.html', {
        'framework_name': 'Django'
    })
# Create your views here.
