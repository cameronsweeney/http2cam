from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host('pokedex', 'pokedex.urls', name='homepage_host'),
    host('latb22', settings.ROOT_URLCONF, name='latb22'),
)