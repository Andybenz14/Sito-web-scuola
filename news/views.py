from django.views import generic
from .models import Post

class PostList(generic.ListView):
    paginate_by = 5
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'notizie.html'


class IndexPostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:5]
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'notizia.html'