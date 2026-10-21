"""
Задание 4:
Придумать класс самостоятельно, реализовать в нем методы экземпляра
класса, статические, методы, методы класса. – 1 – 3 балла
"""
class Book:
    total_books = 0

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        Book.total_books += 1

    def info(self):
        return f"{self.title}, {self.pages} стр."

    @classmethod
    def count(cls):
        return cls.total_books

    @staticmethod
    def is_long(pages):
        return pages > 300


if __name__ == "__main__":
    b1 = Book("Python", 250)
    b2 = Book("Algorithms", 400)
    print(b1.info())
    print(b2.info())
    print(Book.count())
    print(Book.is_long(b2.pages))
