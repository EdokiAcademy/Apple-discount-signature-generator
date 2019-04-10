import requests

def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    print(request)
    return HttpResponse('<pre>' + r.text + '</pre>')