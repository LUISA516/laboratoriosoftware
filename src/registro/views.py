# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from.forms import RegistroForm
from.models import Registro
from django.views.generic import ListView, TemplateView

# Create your views here.

def indexRegistro(request):
	return render(request, 'inicio/index.html')


def registro_view(request):
	if request.method == 'POST':
		form = RegistroForm(request.POST)
		if form.is_valid():
			form.save()
		#return redirect('compra:index_compra')
	else:
		form = RegistroForm()
	return render(request, 'registro/registro_form.html', {'form':form})	