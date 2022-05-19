class Book:
    name = '1984'
    writer = 'Джордж Оруэлл'
    pages = 213


setattr(Book, 'name', 'Скотный двор')
setattr(Book, 'pages', 115)

print(Book.__dict__)

