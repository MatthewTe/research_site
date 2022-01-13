from django.shortcuts import render, redirect

# Importing Blog data models:
from .models import BlogPost

# Create your views here.
def blog_index(request):
    """The main index for rendering the homepage for all blog posts.
    """
    context={}
    return render(request, "blog/blog_index.html", context=context)

def blog_post(request, slug: str = None):
    """The view that renders all the content for a single blog post.
    
    It queries the database for a single blog post via its slug field  (passed into the view as a URL param)
    and passes this data on to the template. If there is no slug with this url it redirects the user
    to the blog home page.

    Args:
        slug (str): The 'slugified' version of the blog's title that is sued to query the single blog post.
            This param is recieved through the URL.
    """
    context = {}
    # If a Blog Post Object is not found, ignore the error and set the post to None:
    try:
        post = BlogPost.objects.get(slug=slug)
    except:
        post = None

    # Redirecting if no blog post found with specific slug:
    if post == None:
        return redirect("blog_home")
    else:
        context["blog_post"] = post
    
    return render(request, "blog/blog_post.html", context=context)