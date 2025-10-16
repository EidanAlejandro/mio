from django.shortcuts import render
from .models import Solicitud

def solicitud_list(request):
    solicitudes = Solicitud.objects.all()  # Obtiene todas las solicitudes
    return render(request, 'requests/solicitud_list.html', {'solicitudes': solicitudes})
