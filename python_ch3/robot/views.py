from django.shortcuts import render


# Create your views here.

def robot(request):
    return render(request, 'robot/robot.html')
