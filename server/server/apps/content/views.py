from django.shortcuts import render
from django.conf import settings

# Create your views here.
def index(request):
    if 'type' in request.session and request.session['type'] in settings.ALLOWED_USERS:
        return render(
            request,
            'index.html',
            {
                'user': request.session['user'],
            },
        )
    else:
        request.session.flush()
        return render(request, 'disallow.html')