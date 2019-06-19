from django.shortcuts import render


# Create your views here.

def hello(request):
    return render(request, 'D:\cafe24\PycharmProjects\python\python_ch3\hello.html')
