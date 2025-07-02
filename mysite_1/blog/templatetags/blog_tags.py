from django import template
from ..models import Post
from django.db.models import Count


register = template.Library()

@register.simple_tag
def total_posts():
    return Post.pub.count()
@register.inclusion_tag('blog/post/latest_post.html')
def show_latest_posts(count=3):
    latest_posts = Post.pub.order_by('-published')[:count]
    return {
        'latest_post':latest_posts,
    }

@register.simple_tag
def get_most_commented_posts(count=3):
    return Post.pub.annotate(
        total_comments=Count('comments')   
    ).order_by('-total_comments')[:count]
@register.filter(name='posts_abouth_helth')
def func(text):
    return ''