from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from articles.models import Article


# Create your views here.


def index(request):
    article_list = Article.objects.all()
    template = loader.get_template('articles/index.html')
    context = RequestContext(request, {
        'article_list':article_list,
    })
    return HttpResponse(template.render(context))

def article_text(request, article_id):
    # Article.objects.get(pk=)
    a = Article.objects.get(pk=article_id)
    return HttpResponse(a.article_text)