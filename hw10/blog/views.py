from django.shortcuts import render
from .models import Post

# Create your views here.
def index1(request):
    posts=Post.objects.all().order_by('-pk')
    return render(request,
                'blog/index1.html',
                  {'posts':posts, 'title':'Blog'},
                  )
def single_post_page(request,pk):
    post=Post.objects.get(pk=pk)
    return render(request,
                  'blog/single_post_page.html',
                  {'post':post},
                  )