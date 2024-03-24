class Book:
    '''Book Class'''
    def __init__(self, title, author, publication_year, isbn):
        self.title = title
        self.author = author 
        self.publication_year = publication_year
        self.isbn = isbn

    
    def get_title(self):
        '''Get the title'''
        return self.title
    

    def get_author(self):
        '''get the author'''
        return self.author
    

    def get_publication_year(self):
        '''get the p_year'''
        return self.publication_year
    

    def get_isbn(self):
        '''get the isbn'''
        return self.isbn
    
    def set_title(self, title):
        '''update title'''
        self.title = title


    def set_author(self, author):
        '''update authror'''
        self.author = author

    
    def set_isbn(self, isbn):
        '''update isbn'''
        self.isbn = isbn 

    
    def set_publication_year(self, p_year):
        '''update publication year'''
        self.publication_year = p_year



class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    
    def add_book(self,title,author,publication_year,isbn):
        isbn_found = False
        for books in self.books:
            if books[0] == isbn:
                isbn_found = True
                print('Isbn in use')
        if not isbn_found:
            new_book = Book(title,author,publication_year,isbn)
            self.books.append([isbn,new_book,False])
            print('Book added')
        
    

    def remove_book(self, title):
        book_found = False
        for book in self.books:
            if book[1].get_title() == title:
                book_found = True
                self.books.remove(book)
                print('Book removed')
        if not book_found:
            print('No book found')

    
    def search_book_by_author(self,author):
        book_found = False
        number_of_books = 0
        for books in self.books:
            if books[1].get_author() == author:
                number_of_books += 1
                print(f'Book number {number_of_books}')
                print(f'Author : {books[1].get_author()}\nTitle : {books[1].get_title()}\nISBN : {books[1].get_isbn()}\nPublication Year : {books[1].get_publication_year()}\n')
                book_found = True
        if not book_found:
            print('No Books found')
    


    def search_book_by_title(self,title):
        book_found = False
        number_of_books = 0
        for books in self.books:
            if books[1].get_title() == title:
                number_of_books += 1
                print(f'Book number {number_of_books}')
                print(f'Author : {books[1].get_author()}\nTitle : {books[1].get_title()}\nISBN : {books[1].get_isbn()}\nPublication Year : {books[1].get_publication_year()}\n')
                book_found = True
        if not book_found:
            print('No Books found')


    def borrow_book(self, title, borrower_name):
        book_found = False
        for books in self.books:
            if books[1].get_title() == title:
                book_found = True
                if books[2] == False:
                    books[2] = True
                    print('Book borrowed')
                else:
                    print('Book Already borrowed')
        if not book_found:
            print('Book not found')


    def return_book(self, title):
        book_found = False
        for books in self.books:
            if books[1].get_title() == title:
                book_found = True
                if books[2] == True:
                    books[2] = False
                    print('Book unborrowed')
                else:
                    print('Book Already unborrowed')
        if not book_found:
            print('Book not found')

    def display_unborrowed_books(self):
        for books in self.books:
            if books[2] == False:
                print(f'Author : {books[1].get_author()}\nTitle : {books[1].get_title()}\nISBN : {books[1].get_isbn()}\nPublication Year : {books[1].get_publication_year()}\n')
            


        
        
    




    