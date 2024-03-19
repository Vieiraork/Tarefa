from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tarefa
from datetime import datetime
from django.db import transaction, DatabaseError

# Create your views here.
def index(request):
    tarefas = Tarefa.objects.all()

    return render(request, 'home.html', {
        'tarefas': tarefas
    })

def create(request):
    return render(request, 'create.html')

def store(request):
    try:
        with transaction.atomic():
            tarefa = Tarefa(
                    no_tarefa   = request.POST.get('no_tarefa'),
                    st_status   = request.POST.get('st_status'),
                    dt_inclusao = datetime.now()
            )
            tarefa.save()
    except DatabaseError as D:
        return HttpResponse(D.with_traceback())
    else:
        return redirect('index')
    
def edit(request, id):
    tarefa = Tarefa.objects.get(pk=id)

    return render(request, 'edit.html', {
        'tarefa': tarefa
    })

def update(request, id):
    try:
        with transaction.atomic():
            Tarefa.objects.filter(pk=id).update(
                no_tarefa    = request.POST.get('no_tarefa'),
                st_status    = request.POST.get('st_status'),
                dt_alteracao = datetime.now()
            )
    except DatabaseError as D:
        return HttpResponse(D.with_traceback())
    else:
        return redirect('index')
    
def destroy(request, id):
    try:
        with transaction.atomic():
            Tarefa.objects.filter(pk=id).delete()
    except DatabaseError as D:
        return HttpResponse(D.with_traceback())
    else:
        return redirect('index')
