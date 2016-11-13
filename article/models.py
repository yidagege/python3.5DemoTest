# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from block.models import Block
import sys 

reload(sys)
sys.setdefaultencoding('utf-8')



class Article(models.Model):	
	block = models.ForeignKey(Block,verbose_name=u"所属版块")
	title = models.CharField(u"文章标题",max_length=100)
	content = models.CharField(u"内容描述",max_length=1000)
	status = models.IntegerField(u"状态",choices=((0,u"正常"),(-1,u"删除")))

	create_timestamp = models.DateTimeField(u"创建时间",auto_now_add=True)
	last_update_timestamp = models.DateTimeField(u"最后更新时间",auto_now=True)


	def __str__(self):
		return self.title;

	class Meta:
		verbose_name = "文章"
		verbose_name_plural = "文章"
