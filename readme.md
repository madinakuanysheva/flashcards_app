# Flashcards App — AI-Powered Learning Through Intelligent Flashcards

**Flashcards App** is a web application designed to make learning new topics faster and more efficient through AI-generated flashcards.

Instead of manually creating study materials, users can simply enter a topic they want to learn. Within seconds, the application generates a personalized set of flashcards using AI. Each user's flashcards are securely stored and remain available for review at any time.

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/madinakuanysheva/flashcards_app.git
cd flashcards_app
```

### 2. Create and activate a virtual environment

**macOS / Linux**

```bash
python -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

### 6. Open the application

Navigate to:

```text
http://127.0.0.1:8000/users/
```

---

## Design and Development

### Concept

The project was created to simplify the process of learning new topics by eliminating the need to manually create flashcards and study materials.

### Architecture

The application is built with Django and follows the Model-View-Controller (MVC) architectural pattern. This provides a clear separation between application logic, data management, and the user interface.

### Core Features

* User registration and authentication
* AI-powered flashcard generation based on user-provided topics
* Persistent storage of user-specific flashcards
* Ability to review previously generated flashcards
* Minimalist and focused user interface

---

## Key Approaches

### Topic-Based Generation

Users can generate a complete set of study materials by entering a single topic instead of manually creating individual flashcards.

### AI-Powered Content Generation

The application uses an AI API to generate flashcards based on the context of the requested topic, allowing users to quickly create relevant learning materials.

### User-Specific Data

Each user has an independent collection of flashcards. This ensures that study materials remain private and personalized to each account.

### Server-Side API Integration

External APIs are accessed exclusively through the server-side application. This prevents API credentials from being exposed on the client side and provides a more secure integration architecture.

---

## Design Trade-offs

* **SQLite instead of PostgreSQL:** SQLite was selected because it is lightweight, requires minimal configuration, and is well suited for development and prototyping.
* **No manual editing:** Generated flashcards cannot currently be edited after creation. Manual editing is planned for a future version.
* **Local-first development:** The current implementation is primarily optimized for local development and prototyping rather than production deployment.

---

## Known Limitations

* AI-generated content may contain inaccuracies, particularly for highly specialized topics.
* Flashcards are not currently categorized by difficulty level.
* Generation time may vary depending on network conditions and API response time.
* The application has not yet been optimized for production-scale deployment.

---

## Tech Stack

| Technology | Purpose                             |
| ---------- | ----------------------------------- |
| Python     | Backend development                 |
| Django     | Web framework and application logic |
| HTML       | Application structure               |
| CSS        | User interface and styling          |
| SQLite3    | Database                            |
| AI API     | Automated flashcard generation      |

### Why Django?

Django was selected because it provides a robust foundation for building web applications while offering built-in support for user authentication, database management, routing, and rapid prototyping.

The framework also provides a straightforward way to integrate external APIs for AI-powered functionality.

---

## Demo

[Watch the project demo on Loom](https://www.loom.com/share/0ddf473eb67348bb9d5ffd5fe7c38daa?sid=34134acf-833e-420a-a802-c4af6e7c8e2b)

The demo demonstrates:

* User registration and authentication
* AI-powered flashcard generation
* Reviewing previously generated flashcards
* Project structure and key design decisions

---

## Project Status

* Public GitHub repository
* Fully functional local development setup
* Server-side API integration
* User-specific flashcard storage
* Manual flashcard editing — planned
* Difficulty levels — planned
* Production deployment — planned

---

## License

This project is available for educational and development purposes.

