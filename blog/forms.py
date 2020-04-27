from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'name',
            'description',
            'date',
            'author'
        ]


class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'name',
            'description',
            'date',
            'author'
        ]


