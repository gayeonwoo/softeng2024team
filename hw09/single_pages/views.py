from django.shortcuts import render


def index(request):
    return render(request, 'single_pages/index.html',{'title':'Home'})

def gypage(request):
    return render(request, 'single_pages/gyPage.html',{'title':'gayeon'})

def kmpage(request):
    return render(request, 'single_pages/kmpage.html',{'title':'KyungMun'})
