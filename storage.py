import csv
from typing import List, Optional
from models import Book


def load_books(filepath: str = "books.csv") -> List[Book]:
    books = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                books.append(Book(
                    author=row["author"],
                    title=row["title"],
                    rating=int(row["rating"]),
                    date_read=row["date_read"]
                ))
    except FileNotFoundError:
        pass
    return books


def save_books(books: List[Book], filepath: str = "books.csv"):
    with open(filepath, "w", encoding="utf-8", newline="") as f:
        fieldnames = ["author", "title", "rating", "date_read"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for book in books:
            writer.writerow({
                "author": book.author,
                "title": book.title,
                "rating": book.rating,
                "date_read": book.date_read
            })


def add_book(book: Book, filepath: str = "books.csv"):
    books = load_books(filepath)
    books.append(book)
    save_books(books, filepath)


def find_book(author: str, title: str, filepath: str = "books.csv") -> Optional[Book]:
    books = load_books(filepath)
    for book in books:
        if book.author == author and book.title == title:
            return book
    return None


def delete_book(author: str, title: str, filepath: str = "books.csv") -> bool:
    books = load_books(filepath)
    original_len = len(books)
    books = [b for b in books if not (b.author == author and b.title == title)]
    if len(books) < original_len:
        save_books(books, filepath)
        return True
    return False