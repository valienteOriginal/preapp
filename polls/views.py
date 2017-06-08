from math import sqrt
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def index(request):
    n = int(request.GET.get('n', 15))
    return HttpResponse("Fibnonci of " + str(n) + " using <br> Normal Approach:" + str(fibnonci_normal(n)) + "  <br> Easy Formula Approach" + str(fibnonci_easy(n)))


def fibnonci_normal(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibnonci_normal(n - 1) + fibnonci_normal(n - 2)


def fibnonci_easy(n):
    return ((1 + sqrt(5))**n - (1 - sqrt(5))**n) / (2**n * sqrt(5))
