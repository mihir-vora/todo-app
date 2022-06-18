from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoTask
from .forms import TODOLISTFORM, EDITLISTFORM
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):

	todos = TodoTask.objects.all()
	print(todos)

	countTodos = todos.count()

	completed_todos = TodoTask.objects.filter(complete=True)
	countCompletedTodos = completed_todos.count()

	unclompletedTask = countTodos - countCompletedTodos

	print(unclompletedTask)




	if request.method == 'POST':
		form = TODOLISTFORM(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = TODOLISTFORM()

	context = {
		'todos' : todos,
		'forms' : form,
		'count_Todos' : countTodos,
		'count_completed_todos' : countCompletedTodos,
		'unclompleted_task' : unclompletedTask,
		'completed_todos' : completed_todos
	}

	return render(request, 'todolist_app/index.html', context)

@login_required
def edit(request, pk):
	editTodos = TodoTask.objects.get(id=pk)
	if request.method == 'POST':
		form = EDITLISTFORM(request.POST, instance=editTodos)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = EDITLISTFORM(instance=editTodos)

	context = {
		'form' : form,
	}

	return render(request, 'todolist_app/edit.html', context)

@login_required
def delete(request, pk):
	deletTodos = TodoTask.objects.get(id=pk)

	if request.method == 'POST':
		deletTodos.delete()
		return redirect('/')
	return render(request, 'todolist_app/delete.html')