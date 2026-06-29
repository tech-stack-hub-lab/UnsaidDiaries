from django.shortcuts import render
from django.views import generic
from .models import Post
from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse

# Create your views here.
# def my_diaries(request):
#     return HttpResponse("Hello, blog!")
class PostList(generic.ListView):
    # model = Post
    queryset = Post.objects.filter(status=1)
    # template_name = "post_list.html"
    template_name = "diaries/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "diaries/post_detail.html",
        {"post": post},
    )  
