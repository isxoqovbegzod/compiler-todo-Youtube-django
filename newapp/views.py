import sys
from django.http import HttpResponseNotFound
from django.template import loader
from django.shortcuts import render, redirect
from .models import Video


# Create your views here.

def index_page(request):
    if request.method == 'POST':
        codearetedata = request.POST['code']
        try:
            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')

            exec(codearetedata)
            sys.stdout.close()

            sys.stdout = original_stdout

            output = open('file.txt', 'r').read()
            return render(request, 'index.html', {'code': codearetedata, 'output': output})
        except Exception as e:
            sys.stdout = original_stdout
            output = e
            return render(request, 'index.html', {'code': codearetedata, 'output': output})

    return render(request, 'index.html')


def handler404(request, exception):
    context = {}
    return render(request, '404.html', context)


def vido_template(request):
    video = Video.objects.all()
    return render(request, 'video_template.html', {'video': video})
