from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.
def all_blogs(request):
    blog_posts = BlogPost.objects.order_by('-date')
    return render(request, 'all_blogs.html', {'blogposts': blog_posts})

def detail(request, blog_id):
    blog = get_object_or_404(BlogPost, pk = blog_id)
    return render(request, 'detail.html', {'blog': blog})