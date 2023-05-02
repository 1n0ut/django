from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("thanks! ")

def user_list(request):
    return render(request,"user_list.html")