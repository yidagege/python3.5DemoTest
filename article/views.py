# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from block.models import Block
from models import Article

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
		title = request.POST["title"]
		content = request.POST["content"]
		if not title or not content:
			return render(request,"article_publish.html",{"b":block,"error":"标题和内容都不能为空！","title":title,"content":content})
		if len(title)>100 or len(content)>10000:
			return render(request,"article_publish.html",{"b":block,"error":"标题或内容太长了！","title":title,"content":content})
		article = Article(block=block,title=title,content=content,status=0)
		article.save()
		return redirect("/article/list/%s" % block_id)