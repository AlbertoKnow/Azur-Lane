from django.shortcuts import render
from .models import Character

# Create your views here.

def index(request):
    characters_list = Character.objects.order_by('nombre')
    context = {
        'characters_list' : characters_list
    }

    return render(request, 'index.html', context)