from django.shortcuts import render,get_object_or_404
from courses.models import Palier,Module
def index(request):
    paliers = Palier.objects.all()
    
    return render(request,"home.html",{"paliers":paliers})
