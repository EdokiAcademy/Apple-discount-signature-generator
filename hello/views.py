from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import json
import uuid
import time
import hashlib
import base64
import os
import django_heroku
from ecdsa import SigningKey
from ecdsa.util import sigencode_der

def index(request):
    payload = request.POST["signature"]
    with open(os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'staticfiles'),"./cert.der"), "rb") as myfile:
        der = myfile.read()
        signing_key = SigningKey.from_der(der)
        signature = signing_key.sign(payload.encode("utf-8"),hashfunc=hashlib.sha256,sigencode=sigencode_der)
        encoded_signature = base64.b64encode(signature)
        encoded_signature = str(encoded_signature, "utf-8")
        return HttpResponse(encoded_signature)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
