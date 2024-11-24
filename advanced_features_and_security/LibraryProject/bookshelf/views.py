from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from myapp.models import Article

@permission_required('myapp.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'myapp/article_list.html', {'articles': articles})

@permission_required('myapp.can_create', raise_exception=True)
def create_article(request):
    if request.method == "POST":
        # Process form submission to create an article
        pass
    return render(request, 'myapp/create_article.html')

@permission_required('myapp.can_edit', raise_exception=True)
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        # Process form submission to edit the article
        pass
    return render(request, 'myapp/edit_article.html', {'article': article})

@permission_required('myapp.can_delete', raise_exception=True)
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect('article_list')
    return render(request, 'myapp/delete_article.html', {'article': article})