from django.shortcuts import render,get_object_or_404
from .models import Post
from django.http import Http404 
from django.core.paginator import Paginator
# Create your views here.
def post_list(request):
    posts = Post.pub.all()

    paginator = Paginator(posts,2)
    page_number = request.GET.get("page", 1)
    posts = paginator.page(page_number)
    return render(
        request,
        'blog/post/list.html',
        {
            "posts":posts,
        }
    )
def post_detail(request,year,month,day,slug):
    post = get_object_or_404(
        Post,
        published__year = year,
        published__month = month,
        published__day = day,
        slug = slug,
        status = Post.Status.PUBLISHED,
    )

    return render(
        request,
        'blog/post/detail.html',
        {
            'post':post,
        }
    )