import json
from typing import List, Optional
from models import Book


def load_books(filepath: str = "books.json") -> List[Book]:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Book.from_dict(item) for item in data]
    except FileNotFoundError:
        return []


def save_books(books: List[Book], filepath: str = "books.json"):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump([book.to_dict() for book in books], f, ensure_ascii=False, indent=2)


def add_book(book: Book, filepath: str = "books.json"):
    books = load_books(filepath)
    books.append(book)
    save_books(books, filepath)


def find_book(author: str, title: str, filepath: str = "books.json") -> Optional[Book]:
    books = load_books(filepath)
    for book in books:
        if book.author == author and book.title == title:
            return book
    return None


def delete_book(author: str, title: str, filepath: str = "books.json") -> bool:
    books = load_books(filepath)
    original_len = len(books)
    books = [b for b in books if not (b.author == author and b.title == title)]
    if len(books) < original_len:
        save_books(books, filepath)
        return True
    return False