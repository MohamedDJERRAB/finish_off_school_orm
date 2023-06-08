# Course: 🧭 Database Adventures Beyond the Basics with SQLAlchemy 📚

## 💻 Requirements
- A computer with Python 3.8+ installed.
- A code editor such as VSCode, PyCharm, or a simple text editor.
- Intermediate understanding of Python programming and SQL.
- Knowledge of SQLite and SQLAlchemy as you will be working with more complex features.
- A Git repository to store your progress. You should create a new branch for each mission, and commit and push your work to your branch regularly.

## 📜 Prologue 
As the Library of Alexandria grew, so did its complexity. It now houses not only books, but also newspapers, journals, and various types of multimedia, each with their own unique attributes and relationships. 

But with the complexity came chaos. Now, the grand library needs a hero who can bring order to this disarray, through the power of SQLAlchemy and SQLite. Are you ready for this challenging quest? 

## 🏹 Missions

### Mission 1: "Constructing Complex Tables" 🛠️
#### Quest
Learn to define more complex tables in SQLAlchemy, such as tables with composite primary keys, unique constraints, and indexes.
#### Challenge
Define tables for 'newspapers', 'journals', and 'multimedia'. Each table should have at least one unique constraint or index. 

### Mission 2: "Navigating Relationships" 🗺️
#### Quest
Understand how to establish many-to-many and one-to-many relationships in SQLAlchemy, and how to navigate these relationships in your queries.
#### Challenge
Create relationships between the 'newspapers', 'journals', 'multimedia', and 'categories' tables. Demonstrate how to navigate these relationships through queries.

### Mission 3: "Evolving the Database" 🧬
#### Quest
Learn how to modify existing tables in SQLAlchemy, such as adding new columns, changing column types, or dropping columns.
#### Challenge
Modify the 'books' table to add a new column 'publisher'. Change the 'year_published' column to a 'date_published' column, and drop the 'description' column.

### Mission 4: "Mastering the Query Language" 🧙
#### Quest
Delve deeper into the power of SQLAlchemy queries. Learn how to write complex queries that involve joins, subqueries, aggregation functions, and window functions.
#### Challenge
Write a query to find the number of items (books, newspapers, etc.) each category has, ranked by the total number of items. The result should include the category name and count of items.

## 🏛️ Library Blueprint

Your library shall contain the following structures:

- Table: books
  - id: INTEGER (Primary Key)
  - title: TEXT
  - author: TEXT
  - publisher: TEXT
  - date_published: DATE

- Table: newspapers
  - id: INTEGER (Primary Key)
  - title: TEXT
  - publisher: TEXT
  - date_published: DATE
  - UNIQUE(title, publisher)

- Table: journals
  - id: INTEGER (Primary Key)
  - title: TEXT
  - publisher: TEXT
  - date_published: DATE
  - issue: INTEGER

- Table: multimedia
  - id: INTEGER (Primary Key)
  - title: TEXT
  - creator: TEXT
  - type: TEXT (e.g., 'video', 'audio')
  - release_date: DATE

- Table: categories
  - id: INTEGER (Primary Key)
  - name: TEXT

- Table: item_categories (Join Table)
  - item_id: INTEGER (Foreign Key referencing item.id)
  - category_id: INTEGER (Foreign Key referencing categories.id)
