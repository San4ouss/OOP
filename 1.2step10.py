class Book:
    name = '1984'
    writer = 'Джордж Оруэлл'
    pages = 213
    rating = 8.7
    genre = 'dystopian'


del Book.pages
delattr(Book, 'writer')
del Book.rating

print(Book.__dict__)
