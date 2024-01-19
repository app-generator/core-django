from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

from .models import *

def index(request):

  context = {
    'date': datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
  }
  return HttpResponse("Hello DJANGO! time is: " + context['date'])
