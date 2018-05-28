"""
URLS
"""

from django.urls import path
from . import views

urlpatterns = [
    path('<uuid:congregation_guid>/', views.detail, name='detail')
]
