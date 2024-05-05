from django.shortcuts import render
from django.views import generic
from . models import Book, Author, BookInstance, Genre


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    num_genres_available = Genre.objects.filter(name='Fantasy').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres_available': num_genres_available,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book