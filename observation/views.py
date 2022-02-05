from django.shortcuts import render
from .models import InfoField,InfoLine
# Create your views here.
def index (request):
    return render(request , 'observation/index.html')
def fields (request):
    fields = InfoField.objects.order_by('date_added')
    context = {'fields' : fields}
    return render(request , 'observation/fields.html' , context)
def field (request , field_id):
    field = InfoField.objects.get(id = field_id)
    infolines = field.infoline_set.order_by('-date_added')
    context = {'field' : field , 'infolines' : infolines}
    return render(request , 'observation/field.html' , context)
