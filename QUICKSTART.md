# 🚀 Quick Start Guide - Lab 1 Todo Application

## Project Overview
A full-stack Todo application with:
- **Backend**: Flask REST API with SQLAlchemy
- **Frontend**: HTML/CSS/JavaScript
- **Database**: SQLite

## 📁 Project Structure
```
lab1/
├── backend/
│   ├── app.py              # Flask application with REST API
│   ├── models.py           # SQLAlchemy Todo model
│   ├── database.py         # Database initialization
│   ├── requirements.txt    # Python dependencies
│   └── setup.sh           # Setup script
├── frontend/
│   ├── index.html         # Main HTML page
│   ├── styles.css         # Styling
│   └── app.js             # Frontend JavaScript
└── .gitignore             # Git ignore rules
```

## 🛠️ Setup Instructions

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Run the setup script (recommended):**
   ```bash
   ./setup.sh
   ```

   **OR manually:**
   ```bash
   # Create virtual environment
   python3 -m venv venv
   
   # Activate virtual environment
   source venv/bin/activate  # On macOS/Linux
   # OR
   venv\Scripts\activate     # On Windows
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Start the Flask server:**
   ```bash
   python app.py
   ```
   
   The API will be available at: `http://localhost:5000`

### Frontend Setup

1. **Open the frontend in a browser:**
   - Simply open `frontend/index.html` in your web browser
   - OR use a local server (recommended):
   
   ```bash
   # From the lab1 directory
   cd frontend
   python3 -m http.server 8000
   ```
   
   Then visit: `http://localhost:8000`

## 🧪 Testing the Application

### 1. Test Backend API Endpoints

**Health Check:**
```bash
curl http://localhost:5000/api/health
```

**Get All Todos:**
```bash
curl http://localhost:5000/api/todos
```

**Create a Todo:**
```bash
curl -X POST http://localhost:5000/api/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Todo", "description": "This is a test", "completed": false}'
```

**Update a Todo (replace {id} with actual ID):**
```bash
curl -X PUT http://localhost:5000/api/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Todo", "completed": true}'
```

**Delete a Todo (replace {id} with actual ID):**
```bash
curl -X DELETE http://localhost:5000/api/todos/1
```

### 2. Test Frontend Integration

1. **Open the frontend** in your browser
2. **Add a new todo:**
   - Fill in the title and description
   - Click "Add Todo"
3. **Mark as complete:**
   - Click the "✓ Complete" button
4. **Edit a todo:**
   - Click the "✏️ Edit" button
   - Modify the details
   - Click "Save Changes"
5. **Delete a todo:**
   - Click the "🗑️ Delete" button
   - Confirm deletion

## 📊 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Health check |
| GET | `/api/todos` | Get all todos |
| POST | `/api/todos` | Create a new todo |
| PUT | `/api/todos/:id` | Update a todo |
| DELETE | `/api/todos/:id` | Delete a todo |

## 🎯 Features

- ✅ Create todos with title and description
- ✅ View all todos in a responsive list
- ✅ Edit todo details
- ✅ Mark todos as complete/incomplete
- ✅ Delete todos
- ✅ Persistent storage with SQLite
- ✅ Clean, modern UI with gradient design
- ✅ Real-time updates
- ✅ CORS enabled for cross-origin requests

## 🐛 Troubleshooting

**Backend won't start:**
- Make sure Python 3.7+ is installed
- Check if port 5000 is available
- Verify virtual environment is activated

**Frontend can't connect to backend:**
- Ensure backend is running on port 5000
- Check browser console for CORS errors
- Verify API_BASE_URL in `frontend/app.js`

**Database errors:**
- Delete `backend/todos.db` and restart the server
- The database will be recreated automatically

## 📝 Development Notes

- The database file (`todos.db`) is created automatically on first run
- All data is stored in SQLite (file-based database)
- CORS is enabled for all origins (development only)
- The frontend uses vanilla JavaScript (no frameworks)

## 🎓 Lab 1 Timeline Completion

- ✅ Step 1: Introduction & Planning (5 min)
- ✅ Step 2: Backend Development (15 min)
- ✅ Step 3: Frontend Development (15 min)
- ✅ Step 4: GitHub Integration (5 min)
- ✅ Step 5: Testing & Verification (5 min)

**Total Time: 45 minutes**

## 🚀 Next Steps

1. Run the backend server
2. Open the frontend in a browser
3. Test all CRUD operations
4. Explore the code and make modifications
5. Push to GitHub if needed

Enjoy building with your Todo application! 🎉