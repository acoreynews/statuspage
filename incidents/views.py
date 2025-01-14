from django.http import HttpResponse
from django.template import loader
from .models import Incident
import datetime

# Create your views here.
def incidents(request):
    myincidents = Incident.objects.all().values()
    template = loader.get_template('all_incidents.html')
    context = {
        'myincidents': myincidents,
    }
    return HttpResponse(template.render(context, request))

      
def details(request, id):
    myincident = Incident.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myincident': myincident,
  }
    return HttpResponse(template.render(context, request))

def main(request):
    myincidents = Incident.objects.filter(status='Investigating').values() | Incident.objects.filter(status='Monitoring').values()
    current_datetime = datetime.datetime.now()
    template = loader.get_template('main.html')
    context = {
        'myincidents': myincidents,
        'current_datetime': current_datetime,
    }
    return HttpResponse(template.render(context, request))

def testing(request):
  myincidents = Incident.objects.all()
  template = loader.get_template('template.html')
  context = {
    'myincidents': myincidents,  
  }
  return HttpResponse(template.render(context, request))