#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Routes for built-in content and templates

Created by: Rui Carmo
License: MIT (see LICENSE for details)
"""

import os, sys, logging, random
import bottle
import app, proxy, utils
from config import settings

log = logging.getLogger()


@bottle.route('/qrcode')
@bottle.view('screens/qrcode')
def qrcode():
    """Renders a QR Code and associated message"""
    app.template_vars.update({
        'title'  : 'DECODE THIS',
        'code'   : 'https://codebits.eu',
        'message': 'Have you checked out the site lately?',
    })
    app.template_vars.update(app.screen)
    return app.template_vars


@bottle.route('/text')
@bottle.view('screens/text')
def textmessage():
    """Renders a text/HTML message"""
    app.template_vars.update({
        'title'  : 'ATTENTION',
        'message': 'This is a generic warning message',
    })
    app.template_vars.update(app.screen)
    return app.template_vars


@bottle.route('/pixelart')
@bottle.view('screens/pixelart')
def pixelart():
    """Renders the pixelart view"""
    app.template_vars.update({
        'title'  : 'Pixelart'
    })
    app.template_vars.update(app.screen)
    return app.template_vars


@bottle.route('/hype/random')
def random_hype():
    """Provides the random imagery for the pixelart view"""
    return bottle.redirect(
        app.local_uri + '/img/hype/' +
        random.choice(
            filter( lambda x: x[0] != '.',
                    os.listdir(os.path.join(app.staticroot, 'img/hype')))
        ), 302)


@bottle.route('/tweets')
@bottle.view('screens/tweets')
def tweets():
    """Renders the twitter stream"""
    app.template_vars.update({
        'title'  : 'Twitter feed',
        'query'  : settings.content.twitter
    })
    app.template_vars.update(app.screen)
    return app.template_vars


@bottle.route('/news/<name>')
@bottle.view('screens/news')
def newsfrom(name):
    """Renders a news feed"""
    try:
        title = {'codebits': 'Codebits', 'sapo': 'Notícias'}[name]
    except:
        title = "News"
    app.template_vars.update({
        'title'  : title,
        'feed'   : name
    })
    app.template_vars.update(app.screen)
    return app.template_vars
    

@bottle.route('/about')
@bottle.view('screens/brand')
def brand():
    """Shows an about page"""
    app.template_vars.update({
        'title'  : 'Branding',
    })
    app.template_vars.update(app.screen)
    return app.template_vars


@bottle.route('/shorten/<name:path>')
def shorten(name):
    """URL shortener handler"""
    return utils.shorten(name)



