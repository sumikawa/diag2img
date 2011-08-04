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
from seqdiag import diagparser, builder, DiagramDraw
from block.views import show, edit

default_page = "QlpoOTFBWSZTWSLcEJkAAObfgEAQUAOADwKh3Ao+59/KMAD1tYJKRtU8k9RkHqANADTT1BIkUAyABoA0DR6gVSRA0ZNADQaABojAvzJx3iRERMo0El6TQVikjcE1aJo6jLmExpLsmb1BgY5xSwk4c56mnqhEqDyOLSxVSTkYq0pStWNpvckzg4uTCnWsiMCNMakdV4Ui9ag2EC1IIIRwLjE6IMYrgpMbGxolBZUteV6lWyooekXUpy+oLpKZmdQX8xiDGogKyCSjSQq0E1MVaBog9ZxxQjG18kGBTKKwUCrFzfxdyRThQkCLcEJk"
type = 'seq'
