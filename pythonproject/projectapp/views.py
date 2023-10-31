from django.http import HttpResponse

from django.shortcuts import render
from . models import Place
from . models import Member
# Create your views here.
def demo(request):
    obj_1=Place.objects.all()
    obj_2 =Member.objects.all()
    return render(request, "index.html",{'result':obj_1,'results':obj_2})

