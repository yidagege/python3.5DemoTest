# -*- coding: utf-8 -*-
from django.db import models
import sys 

class Block(models.Model):
	reload(sys)
	sys.setdefaultencoding('utf-8')
	name = models.CharField(u"板块名称",max_length=100)
	desc = models.CharField(u"板块描述",max_length=100)
	manager_name = models.CharField(u"板块管理员名称",max_length=100)
	status = models.IntegerField(u"状态",choices=((0,u"正常"),(-1,u"删除")))


	def __str__(self):
		return self.name;

	class Meta:
		verbose_name = "版块"
		verbose_name_plural = "版块"