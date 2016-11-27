# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from block.models import Block
from models import Article
from forms import ArticleForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def article_list(request,block_id):
	limit = 5
	page = int(request.GET.get("page_no",1))
	block = Block.objects.get(id=int(block_id))
	article_objs_all = Article.objects.filter(block=block, status=0).order_by("-id")

	p = Paginator(article_objs_all, limit)
	try:
		articles = p.page(page)	
	except PageNotAnInteger:
		articles = p.page(1)
	except EmptyPage:
		articles = p.page(p.num_pages)
	
	return render(request,"article_list.html", {
		"page": page, 
		"articles": articles, 
		"b":block
		})


def article_publish(request,block_id):
	block_id = int(block_id)
	block = Block.objects.get(id=block_id)
	if request.method == "GET":
		article_objs = Article.objects.filter(block=block,status=0).order_by("-id")
		return render(request,"article_publish.html",{"articles":article_objs,"b":block})
	else:
		form = ArticleForm(request.POST)
		if form.is_valid():
			article = form.save(commit=False)
			article.block = block
			article.status = 0
			article.save()
			return redirect("/article/list/%s" % block_id)
		else:
			return render(request,"article_publish.html",{"b":block,"form":form})

def article_detail(request,article_id):
	article_id = int(article_id)
	article = Article.objects.get(id=article_id)
	return render(request,"article_detail.html",{"a":article})