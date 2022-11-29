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
    ctx = {}
    ctx['error'] = False
    if request.method == 'GET':
        try:
            username = request.session['username']
            return redirect('/perfil')
        except KeyError:
            return render(request, 'core/login.html', ctx)
    elif request.method == 'POST':
        try:
            username = request.session['username']
            return redirect('/perfil')
        except KeyError:
            correo = request.POST['correo']
            password = request.POST['password']
            try:
                medico = Medico.objects.get(correo=correo, password=password)
                request.session['username'] = medico.correo
                return redirect('/perfil')
            except Medico.DoesNotExist:
                ctx['error'] = True
            return render(request, 'core/login.html', ctx)

def perfil(request):
    try:
        username = request.session['username']
        return render(request, 'core/perfil.html')
    except KeyError:
        return redirect('/login')

def programacion_cirugia(request):
    try:
        username = request.session['username']
    except KeyError:
        return redirect('/login')

def programacion_pabellon(request):
    try:
        username = request.session['username']
        return render(request, 'core/programacion_pabellon.html')
    except KeyError:
        return redirect('/login')

def reservar_pabellon(request):
    try:
        username = request.session['username']
        return render(request, 'core/reservar_pabellon.html')
    except KeyError:
        return redirect('/login')

def disponibilidad_pabellon(request):
    try:
        username = request.session['username']
        return render(request, 'core/disponibilidad_pabellon.html')
    except KeyError:
        return redirect('/login')

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
        return redirect('/login')

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
        return redirect('/login')

def logout(request):
    request.session.flush()
    return redirect('/login')