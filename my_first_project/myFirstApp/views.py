from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import myFirstApp

def members(request):
  template = loader.get_template('members.html')
  rendered_template = template.render()
  return HttpResponse(rendered_template)
def all_members(request):
  mymembers = myFirstApp.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
      'mymembers': mymembers,
  }
  rendered_template = template.render(context, request)
  return HttpResponse(rendered_template)