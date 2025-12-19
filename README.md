# Portal Inspirart

This project is a tattoo course platform (LMS) with a dark and elegant design.

## Tech Stack

-   **Backend:** Python, Django 5, Django Rest Framework
-   **Frontend:** React, Vite, TypeScript
-   **Styling:** Tailwind CSS
-   **Database:** PostgreSQL
-   **Authentication:** JWT (djangorestframework_simplejwt)

## Getting Started

### Backend

1.  Navigate to the root directory.
2.  Install dependencies: `pip install -r requirements.txt`
3.  Create the database `portal_inspirart_db` in PostgreSQL.
4.  Configure the database connection in `portal_inspirart/settings.py`.
5.  Run migrations: `python manage.py makemigrations` and `python manage.py migrate`
6.  Start the development server: `python manage.py runserver`

The backend will be available at `http://localhost:8000`.

### Frontend

1.  Navigate to the `frontend` directory.
2.  Install dependencies: `npm install`
3.  Start the development server: `npm run dev`

The frontend will be available at `http://localhost:5173`.
