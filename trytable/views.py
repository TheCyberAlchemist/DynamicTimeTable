from django.shortcuts import render

# Create your views here.


def table(request):
	context = {
	'days' : ["MON","TUE","WED","THU","FRI"],
	'intervals' : ["l1","l2","l3"]
	}
	return render(request,"table.html",context)