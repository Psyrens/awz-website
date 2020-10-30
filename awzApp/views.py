from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    txt = """
<h1>This WebSite is Under Construction.</h1>
<p>AWZ-WEBAPP</p>"""
    return HttpResponse(txt)
