from django.http import HttpResponse

def last4(request):
    return HttpResponse ("yoz")


def last5(request):
    return HttpResponse (" yoz yoz")


def last6(request):
    return HttpResponse ("yoz yoz yoz")