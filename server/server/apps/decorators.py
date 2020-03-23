from django.shortcuts import render
from django.conf import settings


def login(function):
    def wrap(request, *args, **kwargs):
        if 'type' in request.session and request.session['type'] in settings.ALLOWED_USERS:
            return function(request, *args, **kwargs)
        else:
            request.session.flush()
            return render(request, 'disallow.html')

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap