from django.shortcuts import render
from django.core.paginator import Paginator
from datetime import time, datetime

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {}

    context['books'] = Book.objects.all()

    return render(request, template, context)


def pub_date_view(request, pub_date):
    template = 'books/books_list.html'

    current_date_books = Book.objects.filter(pub_date=pub_date)
    pub_dates_query = Book.objects.all().values('pub_date')

    dates = sorted(list(set(
        [datetime.combine
         (q['pub_date'], time.min)
            for q in pub_dates_query])
    )
    )

    pages = Paginator(dates, 1)

    page = pages.get_page(dates.index(pub_date) + 1)

    if page.has_previous():
        pr_date = pages.get_page(page.previous_page_number()).object_list[0]
    else:
        pr_date = ''
    if page.has_next():
        next_date = pages.get_page(page.next_page_number()).object_list[0]
    else:
        next_date = ''

    context = {
        'books': current_date_books,
        'pr_date': pr_date,
        'next_date': next_date
    }

    return render(request, template, context)
