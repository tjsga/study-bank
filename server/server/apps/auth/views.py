import json

from oauthlib.oauth2.rfc6749.errors import InvalidGrantError
from requests_oauthlib import OAuth2Session

from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here. 
def login(request):
    oauth = OAuth2Session(settings.CLIENT_ID, redirect_uri=settings.REDIRECT_URI, scope=["read"])
    if "error" in request.GET:
        return redirect(reverse("login"))
    if "code" not in request.GET:
        authorization_url, state = oauth.authorization_url("https://ion.tjhsst.edu/oauth/authorize/")
        return redirect(authorization_url)
    try:
        oauth.fetch_token("https://ion.tjhsst.edu/oauth/token/", code=request.GET["code"], client_secret=settings.CLIENT_SECRET)
        profile = oauth.get("https://ion.tjhsst.edu/api/profile")
        user_data = json.loads(profile.content.decode())
        
        
        request.session["user"] = user_data["ion_username"]
        request.session["type"] = user_data["user_type"]
        return redirect(reverse("index"))
    except InvalidGrantError:
        return redirect(reverse("login"))
        
def logout(request):
    if 'user' in request.session.keys():
        del request.session["user"]
    if 'type' in request.session.keys():
        del request.session["type"]
    return redirect(reverse("index"))