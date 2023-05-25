from django.urls import path
from . import views
from django.views.generic import TemplateView
#from django.views.generic.base import RedirectView

app_name = 'blog'

urlpatterns = [
    path('fbv-index', views.indexView, name = 'fbv-index'),
    #path('go-to-maktabkhooneh', views.RedirectToMaktab.as_view(), name = 'redirect-to-maktabkhooneh'),
    #path("cbv-index", TemplateView.as_view(template_name="index.html"), extra_context ={'name':'pourya'}),
    path('post/', views.PostListView.as_view(), name = 'post-list'),
    #path("cbv-index", views.IndexView.as_view(), name="cbv-index"),
    path("post/<int:pk>/",views.PostDetailView.as_view(), name="post-detail"),
]