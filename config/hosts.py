from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host('www', 'config.urls', name='homepage_host'),
    host('pokedex', 'pokedex.urls', name='pokedex'),
    host('latb22', settings.ROOT_URLCONF, name='latb22'),
)