import json
from django.http import JsonResponse

def api_home(request, *args, **kwarg):
    # request -> HttpRequest -> Django
    # print(dir(request))
    # request.body
    print(request.GET)
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body)
    except:
        pass

    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers) # request.headers
    data['content_type'] = request.content_type
    return JsonResponse(data)