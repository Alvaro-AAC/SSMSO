from django.shortcuts import render, redirect

# Create your views here.

def inicio(request):
    try:
        username = request.session['username']
        return redirect('subdirector/perfil')
    except KeyError:
        return redirect('/login')

def perfil(request):
    try:
        username = request.session['username']
        return render('subdirector/perfil')
    except KeyError:
        return redirect('/login')