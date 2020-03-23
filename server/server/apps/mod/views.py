from django.shortcuts import render, get_object_or_404

from .models import Moderator
from ..course.models import Course

from ..decorators import login
# Create your views here.

@login
def dashboard(request):
    try:
        mod = Moderator.objects.get(username=request.session['user'])
    except Moderator.DoesNotExist:
        return render(request, 'mod/not_mod.html', {'user': request.session['user']})
        
    classes = mod.classes.all()
    if mod.admin:
        classes = Course.objects.all()
    
    if not classes:
        return render(request, 'mod/not_mod.html', {'user': request.session['user']})
    
    return render(request, 'mod/index.html', {'user': request.session['user'], 'classes': classes})
    
