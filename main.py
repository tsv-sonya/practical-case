from datetime import datetime
from models import Book
from storage import load_books, add_book, delete_book
from stats import average_rating, author_statistics, display_all_books


def get_valid_rating() -> int:
    while True:
        try:
            rating = int(input("Оценка (1-5): "))
            if 1 <= rating <= 5:
                return rating
            print("Оценка должна быть от 1 до 5.")
        except ValueError:
            print("Введите число от 1 до 5.")


def menu():
    books = load_books()

    while True:
        print("\n--- Трекер прочитанных книг ---")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")

        choice = input("\nВыберите действие: ")

        if choice == "1":
            print("\n--- Добавление книги ---")
            title = input("Название: ")
            author = input("Автор: ")
            rating = get_valid_rating()
            date_read = datetime.now().strftime("%Y-%m-%d")

            book = Book(author=author, title=title, rating=rating, date_read=date_read)
            add_book(book)
            books = load_books()
            print("Книга добавлена!")

        elif choice == "2":
            books = load_books()
            display_all_books(books)

        elif choice == "3":
            books = load_books()
            if not books:
                print("Нет книг для расчёта оценки.")
            else:
                avg = average_rating(books)
                print(f"\nСредняя оценка: {avg}/5")

        elif choice == "4":
            books = load_books()
            if not books:
                print("Нет книг для статистики.")
            else:
                stats = author_statistics(books)
                print("\n--- Статистика по авторам ---")
                for author, data in stats.items():
                    print(f"\n{author}:")
                    print(f"  Книг: {data['count']}")
                    print(f"  Средняя оценка: {data['avg_rating']}/5")

        elif choice == "5":
            books = load_books()
            if not books:
                print("Список книг пуст.")
                continue
            print("\n--- Удаление книги ---")
            display_all_books(books)
            author = input("Автор удаляемой книги: ")
            title = input("Название удаляемой книги: ")
            if delete_book(author, title):
                books = load_books()
                print("Книга удалена!")
            else:
                print("Книга не найдена.")

        elif choice == "6":
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    menu()