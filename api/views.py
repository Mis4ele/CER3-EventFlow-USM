from rest_framework import viewsets, permissions
from .serializer import EventoSerializer
from UsmCalendar.models import Evento

# Create your views here.


class EventoAdminViewSet(viewsets.ModelViewSet):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()
    permission_classes = [permissions.IsAdminUser]
    def get_queryset(self):
        queryset = Evento.objects.all() #obtiene todo
        fecha_inicio = self.request.query_params.get('fecha_inicio', None)
        tipo = self.request.query_params.get('tipo', None)
        segmento = self.request.query_params.get('segmento', None)
        
        #filtro por año, tipo y segmento
        if fecha_inicio is not None:
            queryset = queryset.filter(fecha_inicio__year=fecha_inicio)
        if tipo is not None:
            queryset = queryset.filter(tipo=tipo)
        if segmento is not None:
            queryset = queryset.filter(segmentos__nombre=segmento) #no funciona el filtro (aun)
        return queryset

class EventoGetViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()

