
from django.urls import path
from hello.views import hello_views, hello_eva, hello_adam, hello_name, hello_template, hello_template2



urlpatterns = [
    path('' ,hello_views), # wyjatek wchodzimy do pustego katalogu czyli bez  /
    path('eva/' ,hello_eva),
    path('adam/' ,hello_adam), #<> to jest zmienna
    path('<str:name>/',hello_name), #<> to jest zmienna

    path('template/<str:name>/', hello_template),
    path('template2/<str:name>/', hello_template2),
]