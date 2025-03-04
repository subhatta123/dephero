from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Simple Test</title>
        </head>
        <body>
            <h1>Simple Test App</h1>
            <p>This is a simple test to verify routing.</p>
            <ul>
                <li><a href="/login">Login</a></li>
                <li><a href="/register">Register</a></li>
            </ul>
        </body>
        </html>
    ''')

@app.route('/login')
def login():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Login Test</title>
        </head>
        <body>
            <h1>Login Page</h1>
            <p>This is a simple login test.</p>
            <form>
                <div>
                    <label>Username:</label>
                    <input type="text" name="username">
                </div>
                <div>
                    <label>Password:</label>
                    <input type="password" name="password">
                </div>
                <button type="submit">Login</button>
            </form>
            <p><a href="/">Back to Home</a></p>
        </body>
        </html>
    ''')

@app.route('/register')
def register():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Register Test</title>
        </head>
        <body>
            <h1>Register Page</h1>
            <p>This is a simple register test.</p>
            <form>
                <div>
                    <label>Username:</label>
                    <input type="text" name="username">
                </div>
                <div>
                    <label>Email:</label>
                    <input type="email" name="email">
                </div>
                <div>
                    <label>Password:</label>
                    <input type="password" name="password">
                </div>
                <div>
                    <label>Confirm Password:</label>
                    <input type="password" name="confirm_password">
                </div>
                <button type="submit">Register</button>
            </form>
            <p><a href="/">Back to Home</a></p>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8501)), debug=True) 