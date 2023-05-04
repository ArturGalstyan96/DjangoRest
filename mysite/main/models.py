from django.db import models

# Create your models here.

class Author(models.Model):
    fname = models.CharField('Author first name: ', max_length=200)
    lname = models.CharField('Author last name: ', max_length=200)
    birth_date = models.DateField('Author birth date')

    def __str__(self):
        return self.fname

class Book(models.Model):

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField('Book name', max_length=100)
    about = models.TextField('Book about')
    creation_date = models.DateField('Book creation date')

    def __str__(self):
        return self.name
