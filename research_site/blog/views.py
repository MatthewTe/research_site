from django.shortcuts import render, redirect
from django.core.paginator import Paginator

# Importing Blog data models:
from .models import BlogPost
from research_core.models import Topic

# Create your views here.
def blog_index(request, topic: str = None):
    """The main index for rendering the homepage for all blog posts.

    The Blog Index view powers two url routes. One url route for blog posts with no topic
    param and one url route that does contain a topic url param: <str:topic>. If the url
    provides a topic param the route filters the BlogPost objects by the topic param.

    Args:

        topic (str|None): The topic that is used to filter the BlogPost's.

    """
    context={}

    # Extracting the request params from the url: 
    search_field = request.GET.get("blog-search", None)
    page_num = request.GET.get("page")

    # Querying all blog posts w/ pagination: 
    if search_field == None:
        posts = BlogPost.objects.all().order_by("-published_at")
    else:
        posts = BlogPost.objects.filter(title__icontains=search_field).all().order_by("-published_at")
    
    # If a topic is provided add a topic filter to the queryset:
    if topic != None:
        posts = posts.filter(topic__topic=topic)

    page_objs = Paginator(posts, 2)
    context["page_obj"] = page_objs.get_page(page_num)

    # Querying the topics to generate the Nav Bar:
    topics = Topic.objects.all()
    context["topics"] = topics
    
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