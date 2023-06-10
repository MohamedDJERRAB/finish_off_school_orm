from sqlalchemy import func
from Mission2 import Session, Book, Category, BookCategory

session = Session()

genre_book_counts = session.query(Category.name, func.count(Book.id).label("book_count")).\
    select_from(Category).join(BookCategory).join(Book).group_by(Category.name).all()

print("Genre   |   Book Count")
print("---------------------")
for genre, book_count in genre_book_counts:
    print(f"{genre:<8} |   {book_count}")

session.close()
