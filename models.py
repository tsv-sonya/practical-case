from dataclasses import dataclass
from datetime import date


@dataclass
class Book:
    author: str
    title: str
    rating: int
    date_read: str

    def __post_init__(self):
        if not 1 <= self.rating <= 5:
            raise ValueError("Оценка должна быть от 1 до 5")

    def to_dict(self):
        return {
            "author": self.author,
            "title": self.title,
            "rating": self.rating,
            "date_read": self.date_read
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            author=data["author"],
            title=data["title"],
            rating=data["rating"],
            date_read=data["date_read"]
        )