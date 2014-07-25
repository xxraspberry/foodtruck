from django.conf.urls import include, patterns, url

urlpatterns = patterns('nearesttrucks.views',
    url(r'^map$', 'map'),
    url(r'^getnearest$', 'getnearest')
)
