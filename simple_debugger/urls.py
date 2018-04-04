from django.urls import path

import nothing.views

urlpatterns = [
    path('', nothing.views.foo),
]
