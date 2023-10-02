from django.shortcuts import render, redirect
from .form import AddSolutionForm

def index(request):
    return render(request, 'index.html')

def add_solution(request):
    if request.method == 'POST':
        form = AddSolutionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddSolutionForm()
    return render(request, 'addsolution.html', {'form': form, 'title': 'Добавление статьи'})
