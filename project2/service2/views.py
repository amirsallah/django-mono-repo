# service1/views.py

from django.http import HttpResponse
from shared.utils import add_numbers

def index(request):
    result = add_numbers(100, 200)
    return HttpResponse(f"Result from service1 is: {result}")

