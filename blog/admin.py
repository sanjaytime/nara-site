from django.contrib import admin
from blog.models import Post, Category, Comment, MarkDownPost
from markdownx.admin import MarkdownxModelAdmin


class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(MarkDownPost, MarkdownxModelAdmin)
