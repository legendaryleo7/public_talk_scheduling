"""
This is views folder for the congregation app
"""
#from django.shortcuts import render
from django.http import HttpResponse
from .models import Congregation

# Create your views here.
def detail(request, congregation_guid):
    """
    This is the main entry point for requesting congregation details
    """
    
    response = Congregation.get(congregation_guid)
    
    return HttpResponse(response)
