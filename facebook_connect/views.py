import urllib
import urlparse
import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

# These probably want to go in settings.py at some point
APP_ID = ""
APP_SECRET = ""

def connect(request):
	redirect_uri = "http://localhost:8000/"
	
	code = request.GET.get('code', None)
	error = request.GET.get('error', None)
	
	if not code or error:
		params = urllib.urlencode({'client_id':APP_ID, 'redirect_uri':redirect_uri, 'scope':'offline_access,email'})
		return render(request, 'facebook_connect/connect.html', {'url': ("https://www.facebook.com/dialog/oauth?%s" % params), 'error':error})
	
	params = urllib.urlencode({'client_id':APP_ID, 'redirect_uri':redirect_uri, 'client_secret': APP_SECRET, 'code': code})
	url = ("https://graph.facebook.com/oauth/access_token?%s" % params)
	response = urllib.urlopen(url).read()
	query = urlparse.parse_qs(response)
	access_token = query.get('access_token')[0]
	#expires = query.get('expires')[0]
	
	params = urllib.urlencode({'access_token':access_token})
	url = ("https://graph.facebook.com/me?%s" % params)
	response = urllib.urlopen(url).read()
	me = json.loads(response)
	
	return HttpResponse(me.get('first_name'))