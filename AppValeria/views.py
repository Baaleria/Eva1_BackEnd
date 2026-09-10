from django.shortcuts import render

def vista_AppValeria(request):
    return render(request, 'AppValeria/AppValeria.html')

def vista_AppValeria2(request):
    return render(request, 'AppValeria/AppValeria2.html')