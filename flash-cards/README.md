# Flashcards App

A flashcards application with **Python** (FastAPI) on the backend and **Next.js** with **ShadCN UI** on the frontend. This app allows users to manage and review flashcards across different categories, such as **General** and **Code**, and provides a clean and modern interface for a seamless user experience.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Backend Requirements](#backend-requirements)
4. [Frontend Requirements](#frontend-requirements)
5. [App Functionalities](#app-functionalities)
6. [Libraries & Dependencies](#libraries--dependencies)
7. [Running the Application](#running-the-application)
8. [Project Structure](#project-structure)
9. [Future Improvements](#future-improvements)

---

## Project Overview

This Flashcards App provides users with an intuitive platform to:
- Create, categorize, and review flashcards.
- Navigate between different categories: **General**, **Code**, and **All Cards**.
- Ensure smooth user navigation and interactive components on the frontend, while utilizing **FastAPI** for managing and storing data on the backend.

---

## Technologies Used

### Backend
- **Python**: Main language for backend development.
- **FastAPI**: Framework for creating APIs and handling backend logic.
- **SQLite**: A lightweight database to store flashcards locally.
- **Uvicorn**: ASGI server to run the FastAPI app.

### Frontend
- **Next.js**: A React-based framework for building the frontend with server-side rendering.
- **ShadCN UI**: A component library that will be used for building the user interface, offering modern and easy-to-use components.

---

## Backend Requirements

### REST API with FastAPI:
[x] **POST `/flashcards/`**: API to create a new flashcard (including title, description, and category).
[x] **GET `/flashcards/`**: Retrieve all flashcards.
[x] **GET `/flashcards/{ID}`**: Retrieve flashcards filtered by ID (General, Code, All Cards).
[x] **DELETE `/flashcards/{id}`**: Delete flashcards by id 

### Database (SQLite):
- Use SQLite to store flashcards with attributes: **title**, **description**, **category**, and **creation date**.

### User Authentication (Optional for Future):
- Implement **JWT** or session-based authentication for users to save their flashcards.

---

## Frontend Requirements

### Pages:
- **Home page (`/`)**: Display a list of flashcards categorized by **General**, **Code**, and **All Cards**. Provide the ability to filter and view flashcards.
- **Create Flashcard page (`/create`)**: Form where users can create new flashcards by entering a title, description, and category.
- **Log-out page (`/logout`)**: Allows users to log out and reset the session (if authentication is implemented).

### Navigation:
- Easy navigation to categories: **General**, **Code**, and **All Cards**.
- Option to switch between categories via a simple UI.

### UI Components:
- Utilize **ShadCN UI** for buttons, forms, and cards to ensure a clean and modern user interface.
- Provide a responsive design that works well on both desktop and mobile devices.

---

## App Functionalities

### Flashcard Creation:
- Allow users to create new flashcards by entering a title, description, and category (e.g., **General**, **Code**).

### Flashcard Categorization:
- Support categorization of flashcards into at least two categories: **General** and **Code**.
- Users can view flashcards sorted by category (General, Code, or All Cards).

### Display Flashcards:
- Flashcards should display the **title**, **description**, and **category**.
- Users can filter and navigate flashcards by category (**General**, **Code**, **All Cards**).

### Log-out Functionality (if authentication is added):
- Users can log out to reset their session and clear any user-specific data.

---

## Libraries & Dependencies

### Backend (Python)
- **FastAPI**: For building the API and handling requests.
- **Uvicorn**: ASGI server to run FastAPI.
- **SQLite**: Lightweight database for storing flashcards locally.
- **Pydantic**: For data validation in FastAPI models.

### Frontend (Next.js)
- **Next.js**: Framework to build the frontend with server-side rendering.
- **ShadCN UI**: Component library for building sleek user interfaces.

---

## Running the Application

### Backend:
- Install Python dependencies (FastAPI, Uvicorn, SQLite, Pydantic).
- Start the FastAPI server to serve flashcard data.

### Frontend:
- Install Node.js dependencies (Next.js, ShadCN UI).
- Run the Next.js application to display the frontend interface.

### Access:
- Visit `http://localhost:3000` in your browser to access the Flashcards App.

---

## Project Structure

