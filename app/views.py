from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from app.models import Category, Game


def home (request) :
    
        
    context = {
        'catgs':Category.objects.all()
    }
    
    games = Game.objects.all()
    
    if 'q' in request.GET :
        q = request.GET['q']
        games = Game.objects.filter(name__icontains=q)

    if 'type' in request.GET :
        g_type = request.GET['type']

        if g_type == 'الكل' : 
            games = Game.objects.all()
        else :
            games = Game.objects.filter(category=Category.objects.get(name=g_type))
            
    context['games'] = games
    
    return render(request,'home.html',context)


def game (request, gameid) :
    game = Game.objects.get(id=gameid)

    return render(request,'game.html',{'game':game})