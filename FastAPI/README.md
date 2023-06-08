# 🚀 Advanced FastAPI Endeavors with SQLAlchemy and API Development 🌐

## 💻 Requirements
- A computer with Python 3.8+ installed. If Python is not yet installed, you can download it from [here](https://www.python.org/downloads/).
- A code editor such as VSCode, PyCharm, or even a simple text editor.
- Advanced understanding of Python programming, SQL, relational databases, SQLAlchemy ORM, and RESTful API principles.
- Familiarity with FastAPI and Uvicorn for building and serving your API.
- Git repository to store your progress. You should create a new branch for each mission, and commit and push your work to your branch regularly. 

## 📜 Prologue 
You've successfully restored the Library of Alexandria's database with the power of SQLAlchemy. Now, it's time to spread the knowledge stored in it to the world, using the power of APIs with FastAPI! But the challenges are getting tougher! Your mission is to implement advanced API features and deliver a stellar experience to the users! 💪🔮

Ready to raise the stakes and challenge your skills? Grab your coding gear, and let the saga continue! 🌟🚀

## 🏹 Missions
Here is your journey broken down into missions and challenges. Each mission has a learning goal and a set of tasks to complete. Work through them, push your code to your branch regularly, and show us what you're made of!

### Mission 1: "Learn to Fly: Basic API with FastAPI" 🌐
#### Quest
Get familiar with FastAPI, learn to build basic API routes, and connect them to the SQLAlchemy models.
#### Challenge
Create basic API routes for all operations (Create, Read, Update, Delete) for each of the `Book`, `Author`, and `Category` models. Ensure the APIs work correctly with your SQLAlchemy models.

### Mission 2: "Handle It: Error Handling and Exceptions" ❌
#### Quest
Learn how to handle different types of errors in FastAPI and provide meaningful error messages to the API users.
#### Challenge
Add exception handling to your API routes. The server should return meaningful error messages for common error scenarios, such as a missing resource, invalid input data, etc.

### Mission 3: "Security First: Authentication and Authorization" 🔒
#### Quest
Understand the importance of security in APIs. Implement authentication and authorization in your API using OAuth2 and JWT.
#### Challenge
Add an authentication route to your API that returns a JWT token. Implement route-level authorization that requires a valid JWT token for accessing certain routes.

### Mission 4: "Upload Knowledge: File Handling in FastAPI" 📂
#### Quest
Learn how to handle file uploads and downloads in FastAPI.
#### Challenge
Create a route for uploading a book cover image, and another route for downloading the uploaded image.

### Mission 5: "Unfolding Pagination and Sorting" 📃
#### Quest
Master the art of organizing data by implementing pagination and sorting on your API.
#### Challenge
Implement pagination and sorting in your API to limit the number of items in response and order them based on different criteria.

### Mission 6: "Crafting the Asynchronous API" ⏱️
#### Quest
Learn how to build high-performance asynchronous APIs with FastAPI and SQLAlchemy.
#### Challenge
Transform your synchronous API into an asynchronous one. Ensure that all operations, including database transactions, are non-blocking.

### Mission 7: "API Versioning & Deployment" 🚀
#### Quest
Grasp the importance of API versioning and master the art of deploying your FastAPI application using Docker.
#### Challenge
Version your API and ensure that it continues to support older versions. Also, dockerize your FastAPI application and prepare it for deployment.

## 🏛️ Endpoints
You shall expose the following routes:

- `GET /books`: Retrieve all books
- `GET /books/{id}`: Retrieve a specific book
- `POST /books`: Create a new book
- `PUT /books/{id}`: Update a specific book
- `DELETE /books/{id}`: Delete a specific book

- `GET /categories`: Retrieve all categories
- `GET /categories/{id}`: Retrieve a specific category
- `POST /categories`: Create a new category
- `PUT /categories/{id}`: Update a specific category
- `DELETE /categories/{id}`: Delete a specific category

- `GET /authors`: Retrieve all authors
- `GET /authors/{id}`: Retrieve a specific author
- `POST /authors`: Create a new author
- `PUT /authors/{id}`: Update a specific author
- `DELETE /authors/{id}`: Delete a specific author

## 📚 Annex - Helpful Resources
Consult the following scrolls of wisdom on your journey:

- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [FastAPI Async & Await](https://fastapi.tiangolo.com/async/)
- [Uvicorn Server](https://www.uvicorn.org/)
- [Python Async IO](https://docs.python.org/3/library/asyncio.html)
- [API Versioning Best Practices](https://restfulapi.net/versioning/)
- [Python Docker Deployment](https://docs.docker.com/samples/python/)
- [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [API Documentation](https://swagger.io/docs/specification/basic-structure/)
- [FastAPI WebSocket](https://fastapi.tiangolo.com/tutorial/websockets/)
- [FastAPI Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/)
