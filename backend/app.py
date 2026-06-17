from flask import Flask, request, jsonify
from flask_cors import CORS
from database import db, init_db
from models import Todo

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Enable CORS for all routes
CORS(app)

# Initialize database
init_db(app)

# Routes

@app.route('/api/todos', methods=['GET'])
def get_todos():
    """Get all todos."""
    try:
        todos = Todo.query.order_by(Todo.created_at.desc()).all()
        return jsonify([todo.to_dict() for todo in todos]), 200
    except Exception as e:
        return jsonify({'error': f'Failed to retrieve todos: {str(e)}'}), 500

@app.route('/api/todos', methods=['POST'])
def create_todo():
    """Create a new todo."""
    try:
        data = request.get_json()
        
        # Validate request data
        if not data:
            return jsonify({'error': 'Request body is required'}), 400
        
        if 'title' not in data:
            return jsonify({'error': 'Title is required'}), 400
        
        if not data['title'].strip():
            return jsonify({'error': 'Title cannot be empty'}), 400
        
        # Create new todo
        new_todo = Todo(
            title=data['title'].strip(),
            description=data.get('description', '').strip(),
            completed=data.get('completed', False)
        )
        
        db.session.add(new_todo)
        db.session.commit()
        
        return jsonify(new_todo.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to create todo: {str(e)}'}), 500

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Update an existing todo."""
    try:
        todo = Todo.query.get(todo_id)
        
        if not todo:
            return jsonify({'error': 'Todo not found'}), 404
        
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Request body is required'}), 400
        
        # Update fields if provided
        if 'title' in data:
            if not data['title'].strip():
                return jsonify({'error': 'Title cannot be empty'}), 400
            todo.title = data['title'].strip()
        
        if 'description' in data:
            todo.description = data['description'].strip()
        
        if 'completed' in data:
            if not isinstance(data['completed'], bool):
                return jsonify({'error': 'Completed must be a boolean'}), 400
            todo.completed = data['completed']
        
        db.session.commit()
        
        return jsonify(todo.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to update todo: {str(e)}'}), 500

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Delete a todo."""
    try:
        todo = Todo.query.get(todo_id)
        
        if not todo:
            return jsonify({'error': 'Todo not found'}), 404
        
        db.session.delete(todo)
        db.session.commit()
        
        return jsonify({
            'message': 'Todo deleted successfully',
            'id': todo_id
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to delete todo: {str(e)}'}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({'status': 'healthy', 'message': 'Todo API is running'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# Made with Bob