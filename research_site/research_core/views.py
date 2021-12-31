from django.shortcuts import render

def site_index(request):
    context = {}
    return render(request, "research_core/website_index.html", context=context)


