# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import *
from django.shortcuts import render

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file


def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

def handle_uploaded_file(f):  
    with open('apps/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk) 

def trabajapaseador(request):
    context = {}
    nombres = request.POST['nombres']
    apellidos = request.POST['apellidos']
    correo = request.POST['correo']
    nacimiento = request.POST['nacimiento'] 
    mensaje = request.POST['mensaje']
    cv = request.FILES['cv']
    handle_uploaded_file(request.FILES['cv']) 
    
    consulta = PostuladorPaseo(nombres=nombres,apellidos=apellidos,correo=correo,nacimiento=nacimiento,mensaje=mensaje,cv=cv)
    consulta.save()
    
    html_template = loader.get_template('home/paseadores.html')
    return HttpResponse(html_template.render(context, request))

def logoutView(request):
    logout(request)
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render({}, request))