# FastAPI Contact Management REST API

This repository contains the source code for an improved version of a REST API application for managing contacts, building upon the previous homework assignment. The API is developed using FastAPI framework and SQLAlchemy ORM for efficient interaction with a PostgreSQL database.

## Features

- **Create a new contact:** Add new contacts to the database with basic information such as first name, last name, email address, phone number, date of birth, and additional data (optional).
- **Retrieve all contacts:** Get a list of all contacts stored in the database.
- **Retrieve contact by ID:** Retrieve detailed information about a contact based on its identifier.
- **Update an existing contact:** Update an existing contact based on the provided ID.
- **Delete a contact:** Remove a contact from the database based on its identifier.
- **Search contacts:** Search for contacts by first name, last name, or email address.
- **Get contacts with upcoming birthdays:** Retrieve a list of contacts whose birthday falls within the next 7 days.

## Technologies

- **FastAPI:** FastAPI is used for rapid development of the API with Python.
- **SQLAlchemy ORM:** SQLAlchemy ORM is employed for seamless interaction with the PostgreSQL database.
- **PostgreSQL:** PostgreSQL serves as the chosen database due to its reliability and scalability.
- **Pydantic:** Pydantic data validation module ensures the validation of input data.

## Documentation

The documentation for this project is generated using Sphinx. All necessary functions and methods in the main modules have been documented with docstrings to facilitate the generation of comprehensive documentation.

## Testing

Unit tests for the repository modules are implemented using the Unittest framework. The `tests/test_unit_repository_notes.py` module serves as a reference for writing unit tests.

Functional tests for any chosen path from the homework assignment are conducted using the Pytest framework to ensure the correctness and reliability of the API endpoints.

## Getting Started

To get started with the project:

1. Install all the required dependencies from the `requirements.txt` file.
2. Configure the connection to the PostgreSQL database in the `.env` file.
3. Run the application using the command `uvicorn main:app --reload`.




