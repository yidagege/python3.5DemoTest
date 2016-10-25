# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from block.models import Block
from models import Article
from forms import ArticleForm

def article_list(request,block_id):
	block_id = int(block_id)
	block = Block.objects.get(id=block_id)
	article_objs = Article.objects.filter(block=block,status=0).order_by("-id")
	return render(request,"article_list.html",{"articles":article_objs,"b":block})

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