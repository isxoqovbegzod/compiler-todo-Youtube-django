from django.shortcuts import render

# Create your views here.

def todo_page(request):
    return render(request, 'todo.html')




