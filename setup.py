import os
import shutil
import sqlite3
from datetime import datetime

def ensure_directories():
    """Ensure all required directories exist"""
    directories = [
        'static',
        'static/logos',
        'static/uploads',
        'static/uploads/logos',
        'frontend',
        'frontend/build',
        'data'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    # Create index.html in frontend/build directory
    index_html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fincode API Server</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: #f5f7fa;
        }
        .container {
            max-width: 800px;
            padding: 40px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        h1 {
            color: #333;
            margin-bottom: 20px;
        }
        p {
            color: #666;
            line-height: 1.6;
            margin-bottom: 20px;
        }
        .button {
            display: inline-block;
            background-color: #4a6cf7;
            color: white;
            padding: 12px 24px;
            border-radius: 4px;
            text-decoration: none;
            font-weight: bold;
            transition: background-color 0.3s;
        }
        .button:hover {
            background-color: #3a5ce5;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Fincode API Server</h1>
        <p>Welcome to the Fincode API Server. The API is running successfully.</p>
        <p>Please use one of the following routes to access the application:</p>
        <p>
            <a href="/login" class="button">Login</a>
            <a href="/register" class="button">Register</a>
        </p>
    </div>
</body>
</html>"""

    # Write the index.html file
    with open('frontend/build/index.html', 'w') as f:
        f.write(index_html_content)
    
    # Create database files if they don't exist
    ensure_database_files()
    
    print("All required directories have been created.")
    print("index.html has been created in frontend/build directory.")

def ensure_database_files():
    """Create database files if they don't exist"""
    # Create users database
    conn = None
    try:
        conn = sqlite3.connect('data/users.db')
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT,
            permission_type TEXT,
            organization_id INTEGER,
            email TEXT,
            created_at TEXT,
            last_login TEXT
        )
        ''')
        
        # Create organizations table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS organizations (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            created_at TEXT
        )
        ''')
        
        # Check if default organization exists
        cursor.execute("SELECT id FROM organizations WHERE name = 'System Organization'")
        if not cursor.fetchone():
            # Insert default organization
            cursor.execute(
                "INSERT INTO organizations (name, created_at) VALUES (?, ?)",
                ('System Organization', datetime.now().isoformat())
            )
        
        conn.commit()
        print("Database files created successfully")
    except Exception as e:
        print(f"Error creating database files: {str(e)}")
    finally:
        if conn:
            conn.close()
    
    # Create tableau data database
    open('data/tableau_data.db', 'a').close()

if __name__ == "__main__":
    ensure_directories() 