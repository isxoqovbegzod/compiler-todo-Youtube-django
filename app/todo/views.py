from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from app.todo.models import ToDo


def todo_page(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        user = request.user
        info = ToDo(todo=word, user=user)
        info.save()
        return redirect('/todo')
    user = ToDo.objects.filter(user=request.user)
    return render(request, 'todo.html', {'user': user})


def delete(request, user, id):
    ToDo.objects.filter(user=user, id=id).delete()
    return redirect('/todo')


def update(request, user, id):
    if request.method == 'POST':
        word = request.POST['word']
        ToDo.objects.filter(user=user, id=id).update(todo=word)
        return redirect('/todo')
    form = ToDo.objects.get(user=user, id=id)
    return render(request, 'update.html', {'form': form})
