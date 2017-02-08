from django.views import generic
from .models import Setup

class IndexView(generic.ListView):
    template_name = 'results/index.html'

    def get_queryset(self):
        return Setup.objects.all()

class DetailView(generic.DeleteView):
    model = Setup
    template_name = 'results/detail.html'
