from django.contrib import admin
from blog.models import Post, Category, Comment
from markdownx.admin import MarkdownxModelAdmin


class PostAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'created_on', 'last_modified')
    list_filter = ('created_on', 'last_modified')
    search_fields = ('title',)

class CategoryAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass



admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)

