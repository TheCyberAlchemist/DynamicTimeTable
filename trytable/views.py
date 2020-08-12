from django.shortcuts import render

# Create your views here.


def table(request):
	context = {
	'days' : ["MON","TUE","WED","THU","FRI"],
	'intervals' : ["a","b","c"]
	}
	return render(request,"table.html",context)