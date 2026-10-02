from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Card

def redirect_view(request, slug):
    try:
        card = Card.objects.get(slug=slug)
        if card.is_active and card.target_url:
            return HttpResponseRedirect(card.target_url)
    except Card.DoesNotExist:
        pass
    
    return render(request, 'inactive.html', {'slug': slug})
