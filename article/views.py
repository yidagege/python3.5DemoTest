from django.shortcuts import render,redirect
from block.models import Block
from models import Article
from django.db.models import Q

def article_list(request,block_id):
	block_id = int(block_id)
	block = Block.objects.get(id=block_id)
	article_objs = Article.objects.filter(block=block,status=0).order_by("-id")
	return render(request,"article_list.html",{"articles":article_objs,"b":block})

def article_publish(request,block_id):
	if request.method == "GET":
		block_id = int(block_id)
		block = Block.objects.get(id=block_id)
		article_objs = Article.objects.filter(block=block,status=0).order_by("-id")
		return render(request,"article_publish.html",{"articles":article_objs,"b":block})
	else:
		if Q(request.POST["title"] == "")|Q(request.POST["content"] == ""):
			return redirect("/article/publish/%s" % block_id)
		else:
			title = request.POST["title"]
			content = request.POST["content"]
			block_id = int(block_id)
			block = Block.objects.get(id=block_id)
			article = Article(block=block,title=title,content=content,status=0)
			article.save()
			return redirect("/article/list/%s" % block_id)