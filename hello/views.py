from django.shortcuts import HttpResponse

def hello_views(request): # request z konwencji , funkcaj musi zwraciac http
    return HttpResponse("hello word") # dopiero widok moze byc str

def hello_eva(request):
    return HttpResponse("helo Eva")

def hello_adam(request):
    return HttpResponse("hello Adam")

def hello_name(request, name):
    return HttpResponse(f"hello {name}")