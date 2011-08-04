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
from nwdiag import diagparser, builder, DiagramDraw
from block.views import show, edit

default_page = "QlpoOTFBWSZTWZtqPoAAAD9ZgEAQQABwCDavnJogAFQlTTSMaQNBmoNpKADR6gGkBefJp1hOwQrgW6hTWFQlmgUo2PqeEk6KuD6iLk9nFT6ZkZmdRQsPUwhj8XckU4UJCbaj6AA="
type = 'nw'
