from django.contrib import admin
from models import Article


class ArticleAdmin(admin.ModelAdmin):
	list_display = ("block","title","content","create_timestamp","last_update_timestamp","status")


admin.site.register(Article,ArticleAdmin)
