from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from django.template.loader import render_to_string


# Create your views here.
def index(request): #HttpRequest
    return HttpResponse("Hello from Django")

def category(request, id=None,category_slug=None):
    if id is not None:
        if id==2:
            raise Http404()
        if id==3:
            return redirect(index)
            #return  redirect("/api/category")
        return HttpResponse(f"Your id is {id}")
    elif category_slug is not None:
        return HttpResponse(f"Your category is {category_slug}")
    return HttpResponse("Hello on my API")

def product(request):
    # t = render_to_string("app/index.html")
    # return HttpResponse(t)
    return render(request, 'app/index.html',{'title':'product','price':200})

def page_not_found(request, exception):
    return HttpResponseNotFound("Page not found")