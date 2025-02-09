from django.http import HttpResponse

def text4(request):
    return HttpResponse ("time")


def text5(request):
    return HttpResponse (" time time")


def text6(request):
    return HttpResponse ("time time time")