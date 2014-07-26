foodtruck
=========

Built with Django 1.6 and Postgres 9.3 (with PostGIS).

To serve in production mode, install uwsgi and nginx, add this to  the first section of /etc/init.d/nginx

    DAEMON_OPTS='-c /opt/foodtruck/nginx.conf'

and then

    uwsgi -i /opt/foodtruck/uwsgi.ini
    sudo service nginx start

To reload uwsgi,

    uwsgi --reload /tmp/uwsgi.pid
