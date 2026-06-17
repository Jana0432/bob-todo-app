#!/bin/bash

echo "🚀 Setting up Flask Todo API Backend..."
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "✅ Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "✨ Setup complete!"
echo ""
echo "To start the backend server:"
echo "  1. Activate the virtual environment: source venv/bin/activate"
echo "  2. Run the server: python app.py"
echo ""
echo "The API will be available at: http://localhost:5000"

# Made with Bob