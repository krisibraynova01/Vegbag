from django.shortcuts import render

from vegbag.blog.models import BlogPost

import random


# Create your views here.
def blog(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog/blog.html', {'blog_posts': blog_posts})


def blog_details(request, pk):
    try:

        blog_post = BlogPost.objects.get(pk=pk)

        all_posts = list(BlogPost.objects.exclude(pk=pk))

        random.shuffle(all_posts)


        related_posts = all_posts[:3]
    except BlogPost.DoesNotExist:

        blog_post = None
        related_posts = None


    return render(request, 'blog/blog-details.html', {'blog_post': blog_post, 'related_posts': related_posts})
