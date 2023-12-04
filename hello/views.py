from django.shortcuts import HttpResponse, render

def hello_views(request): # request z konwencji , funkcaj musi zwraciac http
    return HttpResponse("hello word") # dopiero widok moze byc str

def hello_eva(request):
    return HttpResponse("helo Eva")

def hello_adam(request):
    return HttpResponse("hello Adam")

def hello_name(request, name):
    return HttpResponse(f"hello {name}")

def hello_template(request):
    return HttpResponse ("Hello Eva")

def hello_template2(request,name):
    return render(request,'name_template.html')


