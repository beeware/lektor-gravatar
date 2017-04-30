# -*- coding: utf-8 -*-
from hashlib import md5
from werkzeug.urls import url_encode
from lektor.pluginsystem import Plugin

BASE_URL = 'https://secure.gravatar.com/avatar'

def get_gravatar(email, **options):
    fn = md5(email.lower().strip().encode('utf-8')).hexdigest()
    return '%s/%s?%s' % (BASE_URL, fn, url_encode(options))

class GravatarPlugin(Plugin):
    name = 'Gravatar'
    def on_setup_env(self, **extra):
        self.env.jinja_env.filters['gravatar'] = get_gravatar
