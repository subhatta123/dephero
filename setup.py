import os

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
    
    print("All required directories have been created.")

if __name__ == "__main__":
    ensure_directories() 