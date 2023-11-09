import abc


class Article:
    def __init__(self, title) -> None:
        self.title = title

    def print_title(self):
        print(self.title)
    

class ProvidePages(abc.ABC):
    def get_pages(self):
        raise RuntimeError("Not implemented")
    
    def set_pages(self, pages):
        raise RuntimeError("Not implemented")


class WithAuthor:
    def print_author(self):
        print(self.author)


class WithISDN:
    def print_isdn(self):
        print(self.isdn)

    def generate_barcode(self):
        return "|  ||| || |"


class Book(Article, WithAuthor, WithISDN, ProvidePages):
    def __init__(self, title, author, isdn, pages=500) -> None:
        super().__init__(title)

        self.author = author
        self.isdn = isdn
        self.pages = pages

    def set_pages(self, pages):
        if not isinstance(pages, int):
            raise ValueError("Pages argument should be an integer")

        if pages <= 0:
            raise ValueError("Pages should be > 0")

        self.pages = pages

    def get_pages(self):
        return self.pages


class Report(Article, WithAuthor):
    pass


class Magazine(Article, WithISDN):
    pass


book = Book("J.J. Tolkien", "Lord of the Rings", "123-345-162334")
book.set_pages(648)

magazine = Magazine("Time")

book.print_author()
book.print_isdn()
book.print_title()
print("Number of pages:", book.get_pages())

magazine.print_title()
