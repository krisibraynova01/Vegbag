from django.shortcuts import render

from vegbag.blog.models import BlogPost

import random


# Create your views here.
def blog(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog/blog.html', {'blog_posts': blog_posts})


def blog_details(request, pk):
    try:
        # Retrieve the blog post using the provided primary key (pk)
        blog_post = BlogPost.objects.get(pk=pk)

        # Get all blog posts excluding the current one
        all_posts = list(BlogPost.objects.exclude(pk=pk))

        # Shuffle the list of posts
        random.shuffle(all_posts)

        # Select a subset of posts (e.g., the first 3)
        related_posts = all_posts[:3]
    except BlogPost.DoesNotExist:
        # Handle the case where the blog post does not exist
        blog_post = None
        related_posts = None

    # Render the template with the blog post data and related posts
    return render(request, 'blog/blog-details.html', {'blog_post': blog_post, 'related_posts': related_posts})
