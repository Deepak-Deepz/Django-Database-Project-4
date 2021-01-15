from django.shortcuts import render
from myApp.models import Job
# Create your views here.
def view1(request):
    j = Job.objects.all()
    d = {'jobs' : j}
    return render(request,'myApp/1.html',d)
