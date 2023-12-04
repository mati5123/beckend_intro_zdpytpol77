
from django.urls import path
from hello.views import hello_views, hello_eva, hello_adam, hello_name



urlpatterns = [
    path('' ,hello_views), # wyjatek wchodzimy do pustego katalogu czyli bez  /
    path('eva/' ,hello_eva),
    path('adam/' ,hello_adam), #<> to jest zmienna
    path('<name>/',hello_name), #<> to jest zmienna
]