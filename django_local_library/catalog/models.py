from django.urls import reverse
from django.db import models


from django.db import UniqueConstraint
from django.db.models.functions import Lower

class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a book genre (e.g. Science and Fiction, French Poetry etc.)"
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a particular genre instance"""
        return reverse('genre-detail', args=[str(self.id)])
    

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message = "Genre already exists (case insensitive match)"
            ),
        ]


    class Book(models.Model):
        """Model representing a book (but not a specific copy of a book)"""
        title = models.CharField(max_length=200)
        author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
        summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
        isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')
        genre = models.ManyToManyField('Genre', help_text="Elect a genre for this book")

        def __str__(self):
            """string representation of the Model object"""
            return self.title
        
        def get_absolute_url(self):
            """Returns the url to access a detail record of this book"""
