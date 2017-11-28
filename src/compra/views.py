# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Compra
from.forms import CompraForm
# Create your views here.

def indexCompra(request):
	return render(request, 'inicio/index.html')


def compra_view(request):
	if request.method == 'POST':
		form = CompraForm(request.POST)
		if form.is_valid():
			form.save()
		#return redirect('compra:index_compra')
	else:
		form = CompraForm()
	return render(request, 'compra/form_compras.html', {'form':form})	
