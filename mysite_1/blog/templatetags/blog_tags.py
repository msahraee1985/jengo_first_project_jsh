from django import template
from ..models import Post


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