from typing import List, Dict
from models import Book


def average_rating(books: List[Book]) -> float:
    if not books:
        return 0.0
    return round(sum(book.rating for book in books) / len(books), 1)


def author_statistics(books: List[Book]) -> Dict[str, Dict]:
    stats = {}
    for book in books:
        if book.author not in stats:
            stats[book.author] = {"count": 0, "total_rating": 0, "books": []}
        stats[book.author]["count"] += 1
        stats[book.author]["total_rating"] += book.rating
        stats[book.author]["books"].append(book.title)

    for author in stats:
        stats[author]["avg_rating"] = round(stats[author]["total_rating"] / stats[author]["count"], 1)

    return stats


def display_all_books(books: List[Book]):
    if not books:
        print("Список книг пуст.")
        return
    print("\n--- Все книги ---")
    for book in books:
        print(f"{book.title} - {book.author} | Оценка: {book.rating}/5 | {book.date_read}")