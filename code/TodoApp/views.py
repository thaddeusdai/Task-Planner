from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import random as rd
from django.contrib import messages

from .models import TodoDb
from .forms import TodoForm
from accounts.models import Account
from DataApp.views import create_datatable
import datetime


# Create your views here.
@login_required
def todo(request, _username):
    user = Account.objects.get(username=_username)

    if request.method == "POST":

        form = TodoForm(request.POST or None)

        if form.is_valid():

            if user.tododb_set.filter(task=form.cleaned_data['task']):
                messages.error(
                    request, "Error! Task is already in your todo list.")
            else:
                instance = form.save(commit=False)
                instance.account = request.user
                instance.save()
                messages.success(request, "Task Saved!")

        else:
            messages.error(
                request, "Error! You didn't complete the form properly.")

    task = user.tododb_set.order_by('priority')

    return render(request, 'todo.html', {'task': task, 'user': user})


def post(request, task_id):
    post = TodoDb.objects.get(id=task_id)
    return render(request, 'post.html', {'post': post})


def delete(request, task_id, _username):
    post = TodoDb.objects.get(id=task_id)
    post.delete()

    # when user deletes an item, it means user has completed the task so must update appropriate DataDb
    # adds one to num_of_task for the user on the specific day
    today = datetime.datetime.today().day
    user = Account.objects.get(username=_username)
    if not user.datadb_set.filter(day=today):
        create_datatable(user)
    temp = user.datadb_set.get(day=today)
    temp.num_of_task += 1
    temp.save()

    messages.success(request, "Task Deleted!")

    return redirect("todo", _username)
