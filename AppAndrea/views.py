from django.shortcuts import render

def vista_Andrea(request):
    return render(request,'AppAndrea/vistaAndrea.html')

def vista2_Andrea(request):
    return render (request, 'AppAndrea/vistaAndrea2.html')