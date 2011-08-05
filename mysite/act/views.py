import os
import sys
import base64
import bz2
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.views.decorators.cache import cache_page
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from ConfigParser import SafeConfigParser
from actdiag import diagparser, builder, DiagramDraw, __version__

default_page = "QlpoOTFBWSZTWWnBhfsAACZdgEAQQAIACT4AIgUACiAASEijSPQagEqaGgB6SxHqj644FdKc63jZLbdjwYqMTM0HVNskiCZAwmF8XckU4UJBpwYX7A=="
type = 'act'

@cache_page(60 * 15)
def show(request, diag):
    tree = diagparser.parse(diagparser.tokenize(bz2.decompress(base64.b64decode(diag.replace('-', '/')))))
    diagram = builder.ScreenNodeBuilder.build(tree)
    response = HttpResponse(mimetype='image/png')
    draw = DiagramDraw.DiagramDraw('PNG', diagram, response, antialias=False, font=settings.FONT)
    draw.draw()
    draw.save()
    return response

@csrf_exempt
def edit(request, diag):
    if request.method == 'POST':
        encode = base64.b64encode(bz2.compress(request.POST['diagram'])).replace('/', '-')
        data = simplejson.dumps([{"encode": encode},])
        return HttpResponse(data, mimetype='application/json')
    elif request.method == 'GET':
        if diag == '':
            return HttpResponseRedirect(reverse(settings.SITE_ROOT + type + '.views.edit', args=(default_page,)))
        plain = bz2.decompress(base64.b64decode(diag.replace('-', '/')))
        return render_to_response('diag/edit.html',
                                  {'diag': diag, 'plain': plain, 'type': type, 'vers': __version__})
