"""
Hosts the models that are modifying from the admin section
"""

from django.contrib import admin
from .models import Congregation

# Register your models here.
admin.site.register(Congregation)
