from django.contrib import admin
from django.db import models
from django import forms

from ckeditor.widgets import CKEditorWidget

from redir.models import (Post, Cat)


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = "__all__"


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


admin.site.register(Post, PostAdmin)
admin.site.register(Cat)
