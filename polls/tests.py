from django.test import TestCase

# Create your tests here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Welcome to django')