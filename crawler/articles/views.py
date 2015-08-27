from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from articles.models import Article


# Create your views here.


def index(request):
    page_text = ""
    article_list = Article.objects.all()
    template = loader.get_template('articles/index.html')
    context = RequestContext(request, {
        'article_list':article_list,
    })
    return HttpResponse(template.render(context))
