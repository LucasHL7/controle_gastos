from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transacao
from .form import TransacaoForm
import datetime


def home(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']

    data['now'] = datetime.datetime.now()
    #html = '<html lang="en"><body>It is now %s.</body></html>' % now
    return render(request, 'contas/home.html', data)

def listagem (request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render (request, 'contas/listagem.html', data)

def nova_transacao(request):
    form = TransacaoForm(request.POST or None)
    data = {}
    data['form'] = form

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    return render(request, "contas/form.html", data)