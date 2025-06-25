from django.shortcuts import render,get_object_or_404
from .models import Post
from django.http import Http404 
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import EmailPostForm
from django.core.mail import send_mail
# Create your views here.
def post_list(request):
    posts = Post.pub.all()

    paginator = Paginator(posts,2)
    page_number = request.GET.get("page", 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
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


def post_share(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED,
        
    )
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = f'"{cleaned_data['name']}" recomends you to read "{post.title}"'
            message = f'Read "{post.title}" at {post_url}\n\n\
                "f{cleaned_data['name']}\'s comment:f{cleaned_data['comment']}"\
                '
            from_email = 'A@A.com'
            to = [cleaned_data['to']] 
            send_mail(subject,message,from_email,to)
            sent = True

            
    else:
        form = EmailPostForm()
    return render(
        request,
        'blog/post/share.html',
        {
            'post':post,
            'form':form,
            'sent':sent,
        }

    )