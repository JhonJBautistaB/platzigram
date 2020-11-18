"""Platzigram views."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import pdb
from json import loads, dumps


def hello_world(request):
    """Return a greeting."""
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def sort_integers(request):
    """Return a Json response, sorted numbers request"""
    # Debuber de Django para ver info
    # pdb.set_trace()
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_numbers = sorted(numbers)
    data = dumps({
        'status': 'Ok',
        'numbers': sorted_numbers,
        'message': 'Number Sorted Sucessfully'
    })
    return HttpResponse(data)


def say_hi(request, name, age):
    # pdb.set_trace()
    """ Returna if a users is authorizated """
    if age <12:
        message = f'sorry {name}, you are not allowed here'
    else:
        message = f'¡Hello, {name}! Welcome to Platzigram'
    return HttpResponse(message)