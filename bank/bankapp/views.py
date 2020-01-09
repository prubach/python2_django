from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


# Create your views here.
from .models import Customer


def index(request):
    return HttpResponse('Hello from Bank App')

def test(request):
    body = 'Hello from a template'
    title = 'My first template'
    return render(request, 'bankapp/test.html', {'body_text': body, 'title': title})


def cust(request, cust_id):
    customer = get_object_or_404(Customer, pk=cust_id)
    return render(request, 'bankapp/cust.html', {'customer': customer})