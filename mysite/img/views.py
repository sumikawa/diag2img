import os
import sys
import base64
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from ConfigParser import SafeConfigParser
from nwdiag import diagparser, builder, DiagramDraw

def show(request, diag):
    tree = diagparser.parse(diagparser.tokenize(base64.b64decode(diag)))
    diagram = builder.ScreenNodeBuilder.build(tree)
    response = HttpResponse(mimetype='image/png')

    draw = DiagramDraw.DiagramDraw('PNG', diagram, response, antialias=False)
    draw.draw()
    draw.save()

    return response

def edit(request, diag):
    plain = base64.b64decode(diag);
    return render_to_response('diag/edit.html', {'diag': diag, 'plain': plain})
