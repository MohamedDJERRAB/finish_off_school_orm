from sqlalchemy import func


def category_old_books(session,Book,Categories,book_categories):
    # Query to find the oldest book in each category
    query = session.query(
    Categories.name,
    func.min(Book.year).label('oldest_year')
    ).join(
        book_categories,
        book_categories.category_id == Categories.id
    ).join(
        Book,
        book_categories.book_id == Book.book_id
    ).group_by(Categories.name)
    
    # Execute the query and retrieve the results
    results = query.all()
    
    
    for category_name, oldest_year in results:
        print(f"Category: {category_name} \n Oldest Year: {oldest_year} \n")
        print("------")

