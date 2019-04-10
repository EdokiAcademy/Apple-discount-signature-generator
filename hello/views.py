from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import json
import uuid
import time
import hashlib
import base64
import os
from ecdsa import SigningKey
from ecdsa.util import sigencode_der

def index(request):
    #payload = request.POST["signature"]
    payload = "com.edokicademy.montessoriacademy_K93Z7MT4A2_subscriptionForAYear_50ME_Montessori_1f83d05c-83d1-497e-afad-5d0c4c14bc75_1554909568808"
    with open(os.path.join(STATIC_ROOT,"./cert.der"), "rb") as myfile:
        der = myfile.read()
        signing_key = SigningKey.from_der(der)
        signature = signing_key.sign(payload.encode("utf-8"),hashfunc=hashlib.sha256,sigencode=sigencode_der)
        encoded_signature = base64.b64encode(signature)
        encoded_signature = str(encoded_signature, "utf-8")
        return HttpResponse(request)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
