# Contact Saving App

A simple application for managing contacts. The app loads an initial SQL script and lets you:

- Add contacts  
- Update contacts  
- Delete contacts  

You can run it either with Docker Compose or directly from your terminal.

---

## Tech Stack

- **FastAPI**
- **Uvicorn**
- **MySQL**
- **python-dotenv**
- **Pydantic BaseModel**

---

## Running with Docker Compose

Make sure Docker and Docker Compose are installed, then run:

```bash
docker compose up -d
```

This will start all required services using the `docker-compose.yml` file.

---

## Running Without Docker

Create and activate your virtual environment, install dependencies, then start the app:

```bash
python main.py
```

Make sure your database is running and environment variables are configured.

---

## Environment Variables

Create a `.env` file in the project root and include your database settings:

```env
DB_HOST=localhost
DB_USER=your_user
DB_PASSWORD=your_password
DB_NAME=contacts_db
```

---

## Initial Database

On startup, the application loads the initial SQL query to prepare the database.

---

## API Docs

After running the app, open:

```
http://localhost:8000/docs
```

to explore the interactive Swagger documentation.


