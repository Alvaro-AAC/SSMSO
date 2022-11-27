from django.shortcuts import redirect, render
from .models import *

# Create your views here.

def inicio(request):
    try:
        username = request.session['username']
        return redirect('/perfil')
    except KeyError:
        return redirect('/login')

def login(request):
    try:
        username = request.session['username']
        return redirect('/perfil')
    except KeyError:
        return render(request, 'core/login.html')

def perfil(request):
    try:
        username = request.session['username']
        return render(request, 'core/perfil.html')
    except KeyError:
        # return redirect('/login')
        return render(request, 'core/perfil.html')

def programacion_cirugia(request):
    try:
        username = request.session['username']
        return render(request, 'core/programacion_cirugia.html')
    except KeyError:
        # return redirect('/login')
        return render(request, 'core/programacion_cirugia.html')

def programacion_pabellon(request):
    try:
        username = request.session['username']
        return render(request, 'core/programacion_pabellon.html')
    except KeyError:
        # return redirect('/login')
        return render(request, 'core/programacion_pabellon.html')

def reservar_pabellon(request):
    try:
        username = request.session['username']
        return render(request, 'core/reservar_pabellon.html')
    except KeyError:
        # return redirect('/login')
        return render(request, 'core/reservar_pabellon.html')

def disponibilidad_pabellon(request):
    try:
        username = request.session['username']
        return render(request, 'core/disponibilidad_pabellon.html')
    except KeyError:
        # return redirect('/login')
        return render(request, 'core/disponibilidad_pabellon.html')

def disponibilidad_recursos(request):
    ctx = {
        'recursos': {
            'Insumos disponibles': 15,
            'Unidades de apoyo clínico': 40,
            'Diagnóstico y terapeútico': 90,
            'Recursos humanos': 85,
            'Equipos quirúrgicos': 100,
        }, 
    }
    try:
        username = request.session['username']
        return render(request, 'core/disponibilidad_recursos.html', ctx)
    except KeyError:
        # return redirect('/login')
        return render(request, 'core/disponibilidad_recursos.html', ctx)

def reservar_recursos(request):
    ctx = {
        'recursos': {
            'Insumos disponibles': 15,
            'Unidades de apoyo clínico': 40,
            'Diagnóstico y terapeútico': 90,
            'Recursos humanos': 85,
            'Equipos quirúrgicos': 100,
        }, 
    }
    try:
        username = request.session['username']
        return render(request, 'core/reservar_recursos.html', ctx)
    except KeyError:
        # return redirect('/login')
        return render(request, 'core/reservar_recursos.html', ctx)