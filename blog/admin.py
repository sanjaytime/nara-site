from django.contrib import admin
from blog.models import Post, Category, Comment#, MarkDownPost
from markdownx.admin import MarkdownxModelAdmin


class PostAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'created_date', 'mod_date')
    list_filter = ('created_date', 'mod_date')
    search_fields = ('title',)

class CategoryAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass



admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
# admin.site.register(MarkDownPost, MarkdownxModelAdmin)
