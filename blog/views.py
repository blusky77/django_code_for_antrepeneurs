from django.shortcuts import render, get_object_or_404
from .models import Article
from django.http import Http404
from .forms import ArticleForm, ArticleModelForm
from django.urls import reverse

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)


# Create your views here.
def blog_list_view(request):
    queryset = Article.objects.all()
    context = {
        'article_list': queryset
    }
    return render(request, 'blog/article_list.html', context)


def blog_detail_view(request, pk):
    # obj = get_object_or_404(Article, id=pk)
    try:
        obj = Article.objects.get(id=pk)
    except Article.DoesNotExist:
        raise Http404
    context = {
        'obj': obj
    }
    return render(request, 'blog/article_detail.html', context)


def blog_create_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'blog/article_create.html', context)


class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'

    # queryset = Article.objects.filter(id__gt=1)
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    # success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '/'


class ArticleUpdateView(UpdateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('blog:article-list')