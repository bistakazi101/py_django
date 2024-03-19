from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import member

def members(request):
  mymembers = member.objects.all().values()
  template = loader.get_template('all_memebers.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


# new views 
def details(request,id):
  mymember= member.objects.get(id=id)
  template=loader.get_template("details.html")
  context={
    "mymember":mymember,
  }
  return HttpResponse(template.render(context,request))


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
    