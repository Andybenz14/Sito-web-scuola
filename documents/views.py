from django.views import generic
from .models import Document

# Create your views here.

class DocList(generic.ListView):
    paginate_by = 50
    queryset = Document.objects.order_by('-created_on')
    template_name = 'documents.html'


class SearchResult(generic.ListView):
    paginate_by = 20
    queryset = Document.objects.order_by('-created_on')
    template_name = 'documents.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is None:
            return Document.objects.order_by('-created_on')
        else:
            return Document.objects.filter(name__icontains=query)