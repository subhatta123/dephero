import os
import shutil

def ensure_directories():
    """Ensure all required directories exist"""
    directories = [
        'static',
        'static/logos',
        'static/uploads',
        'static/uploads/logos',
        'data'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    # Ensure index.html exists in static directory
    if not os.path.exists('static/index.html'):
        # If running in Heroku, the app directory might be different
        possible_paths = [
            'static/index.html',
            os.path.join(os.path.dirname(__file__), 'static/index.html')
        ]
        
        source_path = None
        for path in possible_paths:
            if os.path.exists(path):
                source_path = path
                break
        
        if source_path:
            # Copy the index.html to the static directory
            shutil.copy(source_path, 'static/index.html')
    
    print("All required directories have been created.")

if __name__ == "__main__":
    ensure_directories() 