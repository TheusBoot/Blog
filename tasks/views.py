from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Hello(request):
	return HttpResponse('Hello Word')

def taskList(request):
	return render(request, 'tasks/index.html')


def yourname(request, name):
	return render(request, 'tasks/yourname.html', {'name': name})