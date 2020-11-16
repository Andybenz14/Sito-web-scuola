from django.views import generic
from .models import Document

# Create your views here.

class DocList(generic.ListView):
    paginate_by = 5
    queryset = Document.objects.order_by('-created_on')
    template_name = 'documents.html'

class SearchResult(generic.ListView):
    template_name = 'documents.html'