from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')
    list_filter = ('pub_time', )  # 因为这里使用的是tuple，所有当括号里只有一个成员的时候也必须加上末尾的“，”


admin.site.register(Article, ArticleAdmin)
