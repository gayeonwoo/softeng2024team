from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'blog/index1.html'
    ordering='-pk'


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/single_post_page.html'