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
        return render(request, 'subdirector/perfil.html')
    except KeyError:
        # return redirect('/login')
        return render(request, 'subdirector/perfil.html')

def disponibilizar_pabellon(request):
    try:
        username = request.session['username']
        return render(request, 'subdirector/disponibilizar_pabellon.html')
    except KeyError:
        # return redirect('/login')
        return render(request, 'subdirector/disponibilizar_pabellon.html')

def informe(request):
    try:
        username = request.session['username']
        return render(request, 'subdirector/informe.html')
    except KeyError:
        # return redirect('/login')
        return render(request, 'subdirector/informe.html')

def disponibilizar_recursos(request):
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
        return render(request, 'subdirector/disponibilizar_recursos.html', ctx)
    except KeyError:
        # return redirect('/login')
        return render(request, 'subdirector/disponibilizar_recursos.html', ctx)