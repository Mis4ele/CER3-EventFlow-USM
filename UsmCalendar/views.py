from django.shortcuts import render
from .models import Evento, Segmento
from django.utils import timezone

# Create your views here.

def index(request):
    title = "EventFlow"
    # Se guardan los eventos donde la fecha de inicio es mayor o igual a la fecha actual y los ordena de menor a mayor
    Eventos = Evento.objects.order_by('fecha_inicio').filter(fecha_inicio__gte=timezone.now().date())

    # Se obtienen los filtros
    segmento = request.GET.get('selectSegmento')
    tipo = request.GET.get('selectTipo')

    # Si no hay filtros, se seleccionan todos
    if not segmento:
        segmento = "Todos"
    if not tipo:
        tipo = "Todos"

    # Esta parte lo voy a hacer a lo bruto, mi cabeza no rinde ahora mismo como para pensar en cosas complicadas xd
    if segmento == "Todos" and tipo == "Todos":
        EventosSelected = Eventos    
    else:
        EventosSelected = []
        for evento in Eventos:
            if segmento == "Todos" and tipo != "Todos":
                if evento.tipo == tipo:
                    EventosSelected.append(evento)
            elif segmento != "Todos" and tipo == "Todos":
                for evento_segmento in evento.segmentos.all():
                    if str(evento_segmento) == segmento:
                        EventosSelected.append(evento)
                        break
            else:
                if evento.tipo == tipo:
                    for evento_segmento in evento.segmentos.all():
                        if str(evento_segmento) == segmento:
                            EventosSelected.append(evento)
                            break

    data = {
        "title": title,
        "Eventos": Eventos,
        "Segmentos": Segmento.objects.all(),
        "strTipos": Evento.getAllTipos('str'),
        "Tipos": Evento.getAllTipos(''),
        "selectSegmento": segmento,
        "selectTipo": tipo,
        "EventosSelected": EventosSelected,
    }

    return render(request, 'UsmCalendar/index.html', data)