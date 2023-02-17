"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
import math


# /rectangle/area
def rectangle_area(request, length, height):
    area = length * height
    return HttpResponse(
        f"<h1>The area of a rectangle with a length of {length} and a height of {height} is {area}</h1>"
    )


# /rectangle/perimeter
def rectangle_perimeter(request, length, height):
    perimeter = (length + height) * 2
    return HttpResponse(
        f"<h1>The perimeter of a rectangle with a length of {length} and a height of {height} is {perimeter}</h1>"
    )


# /circle/area
def circle_area(request, radius):
    area = (math.pi * radius) ** 2
    return HttpResponse(
        f"<h1>The area of a circle with a radius of {radius} is {area}</h1>"
    )


# /circle/perimeter
def circle_perimeter(request, radius):
    perimeter = (math.pi * radius) * 2
    return HttpResponse(
        f"<h1>The perimeter of a circle with a radius of {radius} is {perimeter}</h1>"
    )


urlpatterns = [
    path("rectangle/perimeter/<int:length>/<int:height>/", rectangle_perimeter),
    path("rectangle/area/<int:length>/<int:height>/", rectangle_area),
    path("circle/area/<int:radius>/", circle_area),
    path("circle/perimeter/<int:radius>/", circle_perimeter),
]
