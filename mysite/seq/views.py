import os
import re
import sys
import base64
import bz2
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.views.decorators.cache import cache_page
from ConfigParser import SafeConfigParser
from seqdiag import diagparser, builder, DiagramDraw

default_page = "QlpoOTFBWSZTWSLcEJkAAObfgEAQUAOADwKh3Ao+59/KMAD1tYJKRtU8k9RkHqANADTT1BIkUAyABoA0DR6gVSRA0ZNADQaABojAvzJx3iRERMo0El6TQVikjcE1aJo6jLmExpLsmb1BgY5xSwk4c56mnqhEqDyOLSxVSTkYq0pStWNpvckzg4uTCnWsiMCNMakdV4Ui9ag2EC1IIIRwLjE6IMYrgpMbGxolBZUteV6lWyooekXUpy+oLpKZmdQX8xiDGogKyCSjSQq0E1MVaBog9ZxxQjG18kGBTKKwUCrFzfxdyRThQkCLcEJk"

@cache_page(60 * 15)
def show(request, diag):
    tree = diagparser.parse(diagparser.tokenize(bz2.decompress(base64.b64decode(diag))))
    diagram = builder.ScreenNodeBuilder.build(tree)
    response = HttpResponse(mimetype='image/png')

    draw = DiagramDraw.DiagramDraw('PNG', diagram, response, antialias=False)
    draw.draw()
    draw.save()

    return response

def edit(request, diag):
    if request.method == 'POST':
        diagram = request.POST['myvalue'];
        diagram = re.sub("^(<br>)+", "", diagram);
        diagram = re.sub("(<br>)+$", "", diagram);
        diagram = re.sub("&lt;","<",diagram);
        diagram = re.sub("&gt;",">",diagram);
        diagram = re.sub("<br>", "\n", diagram);
        encode = base64.b64encode(bz2.compress(diagram));
        return HttpResponseRedirect(reverse(settings.SITE_ROOT + 'seq.views.edit', args=(encode,)))
#       return HttpResponse(request.POST['myvalue'], mimetype='text/html')
    elif request.method == 'GET':
        if diag == '':
            return HttpResponseRedirect(reverse(settings.SITE_ROOT + 'seq.views.edit', args=(default_page,)))
        plain = bz2.decompress(base64.b64decode(diag));
        return render_to_response('diag/edit.html', {'diag': diag, 'plain': plain, 'type': 'seq'})
