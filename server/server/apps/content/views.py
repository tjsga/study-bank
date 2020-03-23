from django.shortcuts import render
from django.conf import settings

from ..decorators import login
from ..mod.models import Moderator

# Create your views here.

@login    
def index(request):
        
    is_mod = Moderator.objects.filter(username=request.session['user']).count() > 0
    
    return render(request, 'index.html', { 'user': request.session['user'], 'is_mod': is_mod} )