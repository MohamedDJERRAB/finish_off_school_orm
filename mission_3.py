

# selecting a book by its author name
def select_book_author(session,Book,author):
    query = session.query(Book).filter(Book.author == "Laura").all()
    for result in query:
        print(result.__dict__)

#delete book
def delete_book(session,Book,id):
    session.query(Book).filter(Book.book_id == id).delete()
    session.commit()

#update book description
def update_book(session,Book,id,new_description):
    session.query(Book).filter(Book.book_id ==id).update({Book.description: new_description})
    session.commit()