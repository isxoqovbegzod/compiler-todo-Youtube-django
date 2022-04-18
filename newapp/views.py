import sys

from django.shortcuts import render


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
