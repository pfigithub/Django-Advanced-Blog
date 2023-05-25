from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView

# Create your views here.

def indexView(request):
    """a function based view to show index page"""

    name = "pourya"
    contex = {'name': name}
    return render(request, 'index.html', contex)



class IndexView(TemplateView):
    """a class based view to show index page"""

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "pourya"
        context['posts'] = Post.objects.all()
        return context
    

'''fbv for redirect'''

class RedirectToMaktab(RedirectView):
    '''redirection view sample for maktabkhooneh'''

    url = 'https://maktabkhooneh.com'

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)




class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 2
    ordering = '-published_date'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["now"] = timezone.now()
    #     return context

class PostDetailView(DetailView):
    model = Post

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["now"] = timezone.now()
    #     return context

