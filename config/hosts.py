from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', 'config.urls', name='homepage_host'),
    host(r'pokedex', 'pokedex.urls', name='pokedex'),
)