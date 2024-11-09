from django.shortcuts import render
import pandas as pd

def index(request):
    return render(request, 'single_pages/index.html',{'title':'Home'})

def gypage(request):
    df = pd.read_csv("single_pages/static/single_pages/gydata.csv")
    post_list = []
    for i, row in df.iterrows():
        post_list.append({
            "title": row["title"],
            "content": row["content"]
        })
    return render(request, 'single_pages/gyPage.html',{'title':'gayeon', 'posts':post_list})

def kmpage(request):
    df = pd.read_csv("single_pages/static/single_pages/kmdata.csv")
    post_list = []
    for i, row in df.iterrows():
        post_list.append({
            "title": row["title"],
            "content": row["content"]
        })
    return render(request, 'single_pages/kmpage.html',{'title':'KyungMun', 'posts':post_list})
