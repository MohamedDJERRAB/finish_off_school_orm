Note : avant d'exécuter  mission 3 il suffit de metre les lignes 34 et 35 en commentaire pour que y'aura pas une erreur de ré-insertion 


# Course: 🚀 Embark on the Database Journey with SQLAlchemy 📚

## 💻 Requirements
- A computer with Python 3.8+ installed. If Python is not yet installed, you can download it from [here](https://www.python.org/downloads/).
- A code editor such as VSCode, PyCharm, or even a simple text editor.
- Basic understanding of Python programming including variables, control flow, functions, and basic data structures like lists and dictionaries.
- Familiarity with SQL and relational databases is beneficial but not mandatory.
- SQLite as your database. SQLite is a software library that provides a relational database management system. Learn more about SQLite from the [SQLite Documentation](https://sqlite.org/docs.html) and [SQLite Python Tutorial](https://www.sqlitetutorial.net/sqlite-python/).
- A Git repository to store your progress. You should create a new branch for each mission, and commit and push your work to your branch regularly. If you need a refresher on Git, you can use this [Git tutorial](https://www.atlassian.com/git/tutorials).

## 📜 Prologue 
In a dimension where data reigns supreme, the ancient Library of Alexandria now faces an existential threat - a threat from the sinister force of data disarray! 🌪️📚

The library's sacred database, once a marvel of organization, is now but a shadow of its former self. Texts and tomes, facts and figures, all now jumbled in a chaotic whirlpool of confusion. It's a data analyst's worst nightmare! 😱

But behold! A prophecy foretells the rise of a brave coder, a true data hero who shall rise from the ranks of the ordinary. This hero shall master the arcane arts of SQLAlchemy, wield the power of SQLite, and restore the library's database to its former glory! 💪🔮

Your quest, brave coder, is filled with perilous challenges and mind-boggling puzzles. But with grit, perseverance, and gallons of coffee, victory is within reach! ☕️🔥

So, are you ready to embark on this epic adventure and etch your name in the annals of coding history? Strap up, for the journey begins NOW! 🌟🚀

## 🏹 Missions
Here is your journey broken down into missions and challenges. Each mission has a learning goal and a set of tasks to complete. Work through them, push your code to your branch regularly, and show us what you're made of!

### Mission 1: "Master the Basics & Engine of Progress" 🎓
#### Quest
Dive into the [SQLAlchemy Codex](https://docs.sqlalchemy.org/en/20/) to understand its core principles. Get a hang of how to create an engine and establish a connection with the sacred database.
#### Challenge
Demonstrate your understanding by writing a Python script that creates an engine and connects it to the Library of Alexandria database. Include comments to explain SQLAlchemy's core principles and how you have applied them in your script.

### Mission 2: "The Library of Alexandria & Filling the Shelves" 📚
#### Quest
Decipher the library's blueprints and use SQLAlchemy ORM to define and create the 'books' table in your database. Populate this table with knowledge.
#### Challenge
Define a 'books' table with columns id, title, author, description, and year_published. Insert five books of your choice into the 'books' table.

### Mission 3: "Seek, Amend, and Erase" 🕵️‍♀️
#### Quest
Delve into the realm of data manipulation in SQLAlchemy. Learn how to retrieve, update, and delete data.
#### Challenge
Create a Python script that retrieves all books written by a specific author, updates a book's description, and deletes a book from the database.

### Mission 4: "The Catalog Codex & Final Ordeal" 📖
#### Quest
Establish relationships between tables in your SQLAlchemy database to create a cataloging system.
#### Challenge
Define a 'categories' table and establish a relationship with 'books'. Use your system to create a query that lists all books within a specific category.

### Mission 5: "Solving Mysteries: Find the oldest book in each category" 📊
#### Quest
Uncover the oldest book within each genre. Use SQLAlchemy queries to retrieve the oldest book from each category.

#### Challenge
Write a query that finds the oldest book in each category, based on the year_published attribute.

### Mission 6: "Author Popularity: Authors with Most Books" 👥
#### Quest
Determine which authors are the most prolific. Use SQLAlchemy queries to calculate the number of books each author has in the library.

#### Challenge
Write a query to find authors who have written the most books. Sort the result in descending order by the count of books.

### Mission 7: "Book Diversity: Authors across Genres" 📚
#### Quest
Identify authors who have written books across multiple genres. Use SQLAlchemy queries to calculate the number of genres each author has written in.

#### Challenge
Write a query that aggregates the number of genres for each author. Use a subquery to select the authors who have written books across the most number of genres.

### Mission 8: "Popular Genres: Books per Genre" 📖
#### Quest
Find out the popularity of genres based on the number of books they have. Use SQLAlchemy queries to calculate the number of books each genre has.

#### Challenge
Write a query that calculates the number of books in each genre by counting the entries in the book_categories join table. Display the genre name and the count of books.


## 🏛️ Library Blueprint

Your library shall contain the following structures:

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

## 📚 Annex - Helpful Resources
Consult the following scrolls of wisdom on your journey:

- [SQLAlchemy ORM Tutorial for Python Developers](https://docs.sqlalchemy.org/en/20/)
- [Python SQLite3 Tutorial](https://docs.python.org/3/library/sqlite3.html)
- [Full Stack Python's Guide to Databases](https://www.fullstackpython.com/databases.html)
- [Python Official Documentation](https://docs.python.org/3/)
- [Database Schema Guide](https://www.lucidchart.com/pages/database-diagram/database-design)

