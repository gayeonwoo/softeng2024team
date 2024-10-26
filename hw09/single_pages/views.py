from django.shortcuts import render
import pandas as pd

# Create your views here.
def landing_page(request):
    return render(request,'single_pages/landing.html', {'title':'landing'})

def kmpage(request):
    return render(request,'single_pages/kmpage.html', {'title': "kmpage"})

def gyPage(request):
    return render(request,'single_pages/gyPage.html', {'title': "gyPage"})

def gy(request):
    df = pd.read_csv("single_pages/static/single_pages/gydata.csv")
    post_list = [
        {"title": row["title"], "content": row["content"]}
        for _, row in df.iterrows()
    ]
    return render(request, 'single_pages/gyPage.html', {'title': 'gayeon Page', 'posts': post_list})

def km(request):
    df = pd.read_csv("single_pages/static/single_pages/kmdata.csv")
    post_list = df.to_dict(orient='records')
    return render(request, 'single_pages/kmpage.html', {'title': 'KyungMun', 'posts': post_list})