# 📝 Bob Todo App

A full-stack Todo application built with Flask (Python) backend and vanilla JavaScript frontend. This project demonstrates a complete CRUD application with RESTful API design, SQLite database integration, and a modern, responsive user interface.

## ✨ Features

- ✅ **Create** todos with title and description
- ✅ **Read** all todos with real-time updates
- ✅ **Update** todo details and completion status
- ✅ **Delete** todos with confirmation
- ✅ **Persistent storage** using SQLite database
- ✅ **RESTful API** with proper error handling
- ✅ **Modern UI** with gradient design and animations
- ✅ **CORS enabled** for cross-origin requests
- ✅ **Comprehensive testing** with pytest

## 🏗️ Architecture

### Backend (Flask)
- **Framework**: Flask with Flask-CORS
- **ORM**: SQLAlchemy
- **Database**: SQLite
- **API**: RESTful endpoints with JSON responses
- **Testing**: pytest with comprehensive test coverage

### Frontend
- **HTML5** for structure
- **CSS3** for styling with modern gradients and animations
- **Vanilla JavaScript** for interactivity (no frameworks)
- **Fetch API** for backend communication

## 📁 Project Structure

```
bob-todo-app/
├── backend/
│   ├── app.py                    # Flask application & API routes
│   ├── models.py                 # SQLAlchemy Todo model
│   ├── database.py               # Database initialization
│   ├── requirements.txt          # Python dependencies
│   ├── setup.sh                  # Automated setup script
│   ├── conftest.py              # pytest configuration
│   ├── test_app.py              # API endpoint tests
│   ├── test_database.py         # Database tests
│   ├── test_models.py           # Model tests
│   ├── API_ENDPOINT_TESTS.md    # API testing documentation
│   └── TEST_DOCUMENTATION.md    # Testing guide
├── frontend/
│   ├── index.html               # Main HTML page
│   ├── styles.css               # Styling
│   └── app.js                   # Frontend JavaScript
├── .gitignore                   # Git ignore rules
├── QUICKSTART.md                # Quick start guide
├── FRONTEND_GUIDE.md            # Frontend documentation
├── LITERATE_CODING_GUIDE.md     # Code documentation guide
└── README.md                    # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- A modern web browser

### Backend Setup

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Run the automated setup script:**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

   **Or set up manually:**
   ```bash
   # Create virtual environment
   python3 -m venv venv
   
   # Activate virtual environment
   source venv/bin/activate  # macOS/Linux
   # OR
   venv\Scripts\activate     # Windows
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Start the Flask server:**
   ```bash
   python app.py
   ```
   
   The API will be available at `http://localhost:5000`

### Frontend Setup

**Option 1: Direct File Access**
- Open `frontend/index.html` directly in your browser

**Option 2: Local Server (Recommended)**
```bash
cd frontend
python3 -m http.server 8000
```
Then visit `http://localhost:8000`

## 🧪 Testing

### Run Backend Tests
```bash
cd backend
source venv/bin/activate  # Activate virtual environment
pytest -v                 # Run all tests with verbose output
pytest --cov=.           # Run tests with coverage report
```

### Test Coverage
- API endpoint tests
- Database operations tests
- Model validation tests
- Error handling tests

See [`backend/TEST_DOCUMENTATION.md`](backend/TEST_DOCUMENTATION.md) for detailed testing information.

## 📡 API Endpoints

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------||
| GET | `/api/health` | Health check | - |
| GET | `/api/todos` | Get all todos | - |
| POST | `/api/todos` | Create new todo | `{"title": "string", "description": "string", "completed": boolean}` |
| PUT | `/api/todos/:id` | Update todo | `{"title": "string", "description": "string", "completed": boolean}` |
| DELETE | `/api/todos/:id` | Delete todo | - |

### Example API Calls

**Create a Todo:**
```bash
curl -X POST http://localhost:5000/api/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn Flask", "description": "Build a REST API", "completed": false}'
```

**Get All Todos:**
```bash
curl http://localhost:5000/api/todos
```

**Update a Todo:**
```bash
curl -X PUT http://localhost:5000/api/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn Flask", "completed": true}'
```

**Delete a Todo:**
```bash
curl -X DELETE http://localhost:5000/api/todos/1
```

## 🎨 UI Features

- **Gradient Background**: Modern purple-to-blue gradient
- **Responsive Design**: Works on desktop and mobile devices
- **Smooth Animations**: Fade-in effects and hover states
- **Status Indicators**: Visual feedback for completed todos
- **Form Validation**: Client-side validation for required fields
- **Confirmation Dialogs**: Prevent accidental deletions

## 🛠️ Technology Stack

### Backend
- **Flask** 2.3.0 - Web framework
- **Flask-CORS** 4.0.0 - Cross-origin resource sharing
- **Flask-SQLAlchemy** 3.0.0 - ORM
- **pytest** 7.4.0 - Testing framework

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with flexbox and grid
- **JavaScript (ES6+)** - Async/await, fetch API

### Database
- **SQLite** - Lightweight, file-based database

## 🐛 Troubleshooting

**Backend won't start:**
- Verify Python 3.7+ is installed: `python3 --version`
- Check if port 5000 is available
- Ensure virtual environment is activated

**Frontend can't connect to backend:**
- Confirm backend is running on port 5000
- Check browser console for CORS errors
- Verify `API_BASE_URL` in `frontend/app.js`

**Database errors:**
- Delete `backend/todos.db` and restart the server
- The database will be recreated automatically

## 📚 Documentation

- [`QUICKSTART.md`](QUICKSTART.md) - Detailed setup and usage guide
- [`FRONTEND_GUIDE.md`](FRONTEND_GUIDE.md) - Frontend architecture and code explanation
- [`backend/TEST_DOCUMENTATION.md`](backend/TEST_DOCUMENTATION.md) - Testing guide
- [`backend/API_ENDPOINT_TESTS.md`](backend/API_ENDPOINT_TESTS.md) - API testing examples
- [`LITERATE_CODING_GUIDE.md`](LITERATE_CODING_GUIDE.md) - Code documentation standards

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🎯 Future Enhancements

- [ ] User authentication and authorization
- [ ] Todo categories and tags
- [ ] Due dates and reminders
- [ ] Search and filter functionality
- [ ] Dark mode toggle
- [ ] Export/import todos
- [ ] Priority levels
- [ ] Subtasks support

## 👨‍💻 Author

Built with ❤️ using Bob AI Assistant

---

**Made with Bob** 🤖