from django.contrib import admin 

from books.models import Book

# class BookAdmin(admin.ModelAdmin):
#     list_display = ('name', 'author', 'pub_date',)

#     list_filter = ('pub_date',)


# admin.site.register(Book, BookAdmin)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'pub_date')

    list_filter = ('pub_date',)

    