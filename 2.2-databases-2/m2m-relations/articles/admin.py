from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Article, Tag, Scope


class ScopeInlineFormSet(BaseInlineFormSet):
    def clean(self):

        main_tags = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_tags += 1
        
        if main_tags > 1: 
            raise ValidationError('Главным может быть только один раздел')
        if main_tags == 0: 
            raise ValidationError('У статьи должен быть один главный раздел')
        
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormSet
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at']
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
