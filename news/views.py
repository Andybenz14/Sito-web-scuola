from django.shortcuts import render

# Create your views here.

def notizie(request):
    return render(request, "notizie.html")

from django.views import generic
from .models import Post

class PostList(generic.ListView):
    paginate_by = 5
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'notizie.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'notizia.html'