import json
import uuid
import time
import hashlib
import base64
from ecdsa import SigningKey
from ecdsa.util import sigencode_der

with open("cert.der", "rb") as myfile:
    payload = "com.edokicademy.montessoriacademy_K93Z7MT4A2_subscriptionForAYear_50ME_Montessori_1f83d05c-83d1-497e-afad-5d0c4c14bc75_1554909568808"
    der = myfile.read()
    signing_key = SigningKey.from_der(der)
    signature = signing_key.sign(payload.encode("utf-8"),hashfunc=hashlib.sha256,sigencode=sigencode_der)
    encoded_signature = base64.b64encode(signature)
    print(str(encoded_signature, "utf-8"))