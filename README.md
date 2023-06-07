# Course: Embark on the Database Journey with SQLAlchemy

## Requirements
- A computer with Python 3.8+ installed. If Python is not yet installed, you can download it from [here](https://www.python.org/downloads/).
- A code editor such as VSCode, PyCharm, or even a simple text editor.
- Basic understanding of Python programming including variables, control flow, functions, and basic data structures like lists and dictionaries.
- Familiarity with SQL and relational databases is beneficial but not mandatory.
- SQLite as your database. SQLite is a software library that provides a relational database management system. Learn more about SQLite from the [SQLite Documentation](https://sqlite.org/docs.html) and [SQLite Python Tutorial](https://www.sqlitetutorial.net/sqlite-python/).
- A Git repository to store your progress. You should create a new branch for each mission, and commit and push your work to your branch regularly. If you need a refresher on Git, you can use this [Git tutorial](https://www.atlassian.com/git/tutorials).

## Prologue
You've been selected by the Guild of Coders to save the ancient Library of Alexandria, under threat from the chaos of data mismanagement. Your quest? Master the mystical arts of SQLAlchemy, using SQLite as your database, and rebuild the library's database. Your journey begins now!

## Mission 1: "Master the Basics & Engine of Progress"
### Quest
Use the [SQLAlchemy Codex](https://docs.sqlalchemy.org/en/20/) to understand its core principles. Learn how to create an engine and establish a connection with the sacred database.
### Challenge
Write a script that creates an engine and a connection to the Library of Alexandria database. Remember, the Guild is looking for understanding and application. Explain SQLAlchemy's core principles and how they are applied in your script.

## Mission 2: "The Library of Alexandria & Filling the Shelves"
### Quest
Use the blueprints of the Library given to you and SQLAlchemy ORM to define and create the books table in your database. Fill it with knowledge.
### Challenge
Define a books table with columns id, title, author, description, and year_published. Insert five books of your choice into the books table.

Library Blueprint:
- Table: books
  - id: INTEGER (Primary Key)
  - title: TEXT
  - author: TEXT
  - description: TEXT
  - year_published: INTEGER

- Table: categories
  - id: INTEGER (Primary Key)
  - name: TEXT

- Table: book_categories (Join Table)
  - book_id: INTEGER (Foreign Key referencing books.id)
  - category_id: INTEGER (Foreign Key referencing categories.id)


## Mission 3: "Seek, Amend, and Erase"
### Quest
A test of your wisdom and adaptability. Retrieve data, amend outdated descriptions, and erase cursed books.
### Challenge
Retrieve all books by your favorite author from the books table. Update the description of a book and erase a cursed book from the books table.

## Mission 4: "The Catalog Codex & Final Ordeal"
### Quest
Build a new cataloging system by establishing relationships between books and categories. With this, you'll reach the climax of your quest - a final test of your mastery of SQLAlchemy.
### Challenge
Create a categories table and establish a relationship with books. Write a query that lists books in a specific category. Lastly, write a comprehensive Python script that demonstrates all you've learned. Include setup, creating tables, inserting data, querying, updating, deleting data, and joining data from related tables.

## Mission 5: "Library Analytics: Genre Distribution"
### Quest
Explore the distribution of book genres in the library. Use CTEs to analyze the number of books in each genre.
### Challenge
Write a CTE that calculates the count of books in each genre and presents the results in descending order. Display the genre and the corresponding book count.

## Mission 6: "User Recommendations: Similar Interests"
### Quest
Help users discover new books by recommending titles based on their interests. Utilize subqueries to find users with similar interests and suggest books they might like.
### Challenge
Write a subquery to find users who have read books by the same author as a given user. Use the results to recommend books that these similar users have enjoyed but the current user has not yet read.

## Mission 7: "Popular Authors: Top Borrowed Books"
### Quest
Determine the most popular authors based on the number of times their books have been borrowed. Employ CTEs and subqueries to calculate the borrow count for each author.
### Challenge
Write a CTE that aggregates the borrow count for each book by author. Use a subquery to select the top authors with the highest combined borrow count across all their books.

## Mission 8: "Book Availability: Available Copies"
### Quest
Track the availability of books in the library. Utilize CTEs and subqueries to calculate the number of available copies for each book.
### Challenge
Write a CTE that calculates the number of available copies for each book by subtracting the number of borrowed copies from the total copies. Present the book title, author, and available copy count.

## Annex - Helpful Resources
- [SQLAlchemy ORM Tutorial for Python Developers](https://docs.sqlalchemy.org/en/20/)
- [Python SQLite3 Tutorial](https://docs.python.org/3/library/sqlite3.html)
- [Full Stack Python's Guide to Databases](https://www.fullstackpython.com/databases.html)
- [Python Official Documentation](https://docs.python.org/3/)
- [Database Schema Guide](https://www.lucidchart.com/pages/database-diagram/database-design)

Remember to consult these resources and others available on the Internet. Good luck on your journey, adventurer! The Guild of Coders awaits your success.
