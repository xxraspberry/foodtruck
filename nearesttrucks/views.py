
import json
from random import randint
import traceback

from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_protect

from nearesttrucks.models import FoodTruck


def map(request):
    template = loader.get_template('map.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def getnearest(request):
    lat = request.GET.get('latitude')
    lng = request.GET.get('longitude')
    limit = 10
    try:
        # constrain limit to be within [10, 100]
        limit = max(10, min(100, int(request.GET.get('limit'))))
    except:
        pass

    try:
        # sort by distance to the specified location
    	sql = '''SELECT id, applicant, fooditems, loc_desc, latitude, longitude, schedule
            FROM nearesttrucks_foodtruck
    	    ORDER BY nearesttrucks_foodtruck.geom <-> 
                st_setsrid(st_makepoint(%s, %s),4326) 
            LIMIT ''' + str(limit)

    	points = []
        for t in FoodTruck.objects.raw(sql, params=(lng, lat)):
        	points.append({
                "lat": t.latitude, 
                "lng": t.longitude,
                "applicant": t.applicant, 
                "schedule": t.schedule, 
                "items": t.fooditems, 
                "loc_desc": t.loc_desc 
            })
        retval = {'points': points}

    except Exception as err:
        print err
        retval = {'error': str(err)}

    return HttpResponse(json.dumps(retval), content_type='application/json')	
