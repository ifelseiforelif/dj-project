from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def index(request): #HttpRequest
    return HttpResponse("Hello from Django")

def category(request, id=None,category_slug=None):
    if id is not None:
        return HttpResponse(f"Your id is {id}")
    elif category_slug is not None:
        return HttpResponse(f"Your category is {category_slug}")
    return HttpResponse("Hello on my API")

def page_not_found(request, exception):
    return HttpResponseNotFound("Page not found")