from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from articles.models import Article,Tag


# Create your views here.


def index(request):
    article_list = Article.objects.order_by("pub_date").reverse()
    template = loader.get_template('articles/index.html')
    
    html = template.render(
        {
        'article_list':article_list,
        'all_tags':Tag.objects.all(),
        },request
    )
    return HttpResponse(html)

def tag_roundup(request,tag_name):
    article_list = None
    tag = Tag.objects.filter(tag_name=tag_name)
    if tag:
        article_list = tag[0].tagged_articles.order_by("pub_date").reverse()

    template = loader.get_template('articles/index.html')
    context = RequestContext(request, {
        'article_list':article_list,
        'all_tags':Tag.objects.all(),
        'tag':tag_name,
    })
    return HttpResponse(template.render(context))

def article_text(request, article_id):
    # Article.objects.get(pk=)
    a = Article.objects.get(pk=article_id)
    return HttpResponse(a.article_text)
