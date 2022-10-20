from django.contrib import admin

from .models import (Comment,
                     Follow,
                     Group,
                     Post)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text', 'group',)
    list_filter = ('pub_date',)
    empty_value_display = '-empty-'


class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'slug',
        'description',
    )
    search_fields = ('slug',)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'author',
        'text',
        'created',
    )
    search_fields = ('author',)


class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'following',
    )
    search_fields = ('user', 'following',)
    list_filter = ('user', 'following',)


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
