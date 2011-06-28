import os
import re
import sys
import base64
import bz2
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.views.decorators.cache import cache_page
from ConfigParser import SafeConfigParser
from nwdiag import diagparser, builder, DiagramDraw

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
    plain = bz2.decompress(base64.b64decode(diag));
    return render_to_response('diag/edit.html', {'diag': diag, 'plain': plain})

def json(request):
    if request.method == 'POST':
        diagram = request.POST['myvalue'];
        diagram = re.sub("(<br>)+$", "", diagram);
        diagram = re.sub("&lt;","<",diagram);
        diagram = re.sub("&gt;",">",diagram);
        diagram = re.sub("<br>", "\n", diagram);
        encode = base64.b64encode(bz2.compress(diagram));
    return HttpResponseRedirect(reverse('mysite.img.views.edit', args=(encode,)))
#    return HttpResponse(request.POST['myvalue'], mimetype='text/html')
