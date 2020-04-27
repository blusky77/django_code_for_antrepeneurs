from django.urls import path
from .views import blog_list_view, blog_detail_view, blog_create_view

from .views import (
    ArticleDetailView,
    ArticleListView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
)


app_name = 'blog'

urlpatterns = [
    # path('', blog_list_view, name='blog_list'),
    path('', ArticleListView.as_view(), name='article-list'),
    # path('<int:pk>/', blog_detail_view, name='detail_view'),
    # path('<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:id>', ArticleDetailView.as_view(), name='article-detail'),
    # path('create/', blog_create_view, name='create_view'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete')
]