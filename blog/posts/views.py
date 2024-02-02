from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def readAllPost(request):
    pass

def create_post(request):
    pass


def readpost(request):
    template = loader.get_template('smain.html')
    return HttpResponse(template.render())
