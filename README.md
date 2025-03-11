# Python Flask Tutorial with Flask-Security

![banner](./images/banner.jpg)

![Flask Logo](https://github.com/NguyenHHKiet/BOOKSTORE-MANAGEMENT-TOPIC/assets/52524133/4bdebee6-66e3-40e2-bc59-f188b1e8cf92)

Flask is a lightweight and flexible Python web framework, perfect for beginners looking to build small websites or learn web development with Python. This tutorial introduces Flask along with **[Flask-Security](https://flask-security-too.readthedocs.io/en/stable/index.html)**, a powerful library that adds essential security features to your Flask applications with minimal effort.

---

## What is Flask-Security?

Flask-Security enhances your Flask application by providing a suite of common security mechanisms, including:

- **Authentication**: Supports session-based, Basic HTTP, or token-based authentication.
- **User Registration**: Optional feature for user sign-up.
- **Role and Permission Management**: Assign roles and permissions to users.
- **Account Activation**: Optional email confirmation for new accounts.
- **Password Management**: Optional password recovery and reset functionality.
- **Two-Factor Authentication**: Optional 2FA support.
- **WebAuthn Support**: Optional biometric or hardware-based authentication.
- **Social/OAuth Authentication**: Optional login via Google, GitHub, etc.
- **Change Email**: Optional email update feature.
- **Login Tracking**: Optional tracking of user logins.
- **JSON/Ajax Support**: Built-in support for modern web applications.

### Integrated Libraries

Flask-Security leverages the following Flask extensions and libraries to deliver its features:

- Flask-Login
- Flask-Mailman
- Flask-Principal
- Flask-WTF
- itsdangerous
- passlib
- QRCode
- webauthn
- authlib

### Supported Data Persistence Options

Flask-Security works seamlessly with popular database libraries:

- Flask-SQLAlchemy
- MongoEngine
- Peewee Flask Utils
- PonyORM (Note: Currently not working - contributions welcome!)
- SQLAlchemy Sessions
- Flask-SQLAlchemy-Lite

---

## Prerequisites

Before getting started, ensure you have the following installed:

- **Python 3.7+**: Download from [python.org](https://www.python.org/downloads/).
- **pip**: Python’s package manager (usually included with Python).
- A terminal or command-line interface (e.g., Command Prompt, PowerShell, or Bash).

---

## Installation

Follow these steps to set up Flask and Flask-Security in your project.

### 1. Create a Virtual Environment

A virtual environment keeps your project dependencies isolated.

```bash
python -m venv .venv
```

Activate it:

- **Windows**: `.venv\Scripts\activate`
- **MacOS/Linux**: `source .venv/bin/activate`

You’ll see `(.venv)` in your terminal when it’s active.

### 2. Install Flask

Use pip to install Flask:

```bash
pip install flask
```

### 3. Install Flask-Security

To add Flask-Security and its dependencies:

```bash
pip install flask-security-too
```

### 4. (Optional) Install a Database Library

If you plan to use a database, install one of the supported options. For example:

```bash
pip install flask-sqlalchemy
```

---

## Usage

### 1. Configure Flask Environment Variables

Set up environment variables to run your app:

- **Windows**:

  ```bash
  set FLASK_APP=run.py
  set FLASK_DEBUG=1
  ```

- **MacOS/Linux**:

  ```bash
  export FLASK_APP=run.py
  export FLASK_DEBUG=1
  ```

- `FLASK_APP`: Specifies the entry point of your app.
- `FLASK_DEBUG=1`: Enables debug mode for live reloading and error details.

### 2. Run the Application

Start the Flask development server:

```bash
python -m flask run
```

OR

```bash
python run.py
```

Visit `http://127.0.0.1:5000/` in your browser to see "Hello, Flask with Security!".

### 4. Explore Flask in the Python Interpreter

To experiment with Flask interactively:

```bash
python
>>> import flask
>>> flask.__version__  # Check the installed version
>>> exit()
```

---

## Managing Dependencies

To share your project or deploy it, use a `requirements.txt` file.

### 1. Generate `requirements.txt`

After installing all packages, run:

```bash
pip freeze > requirements.txt
```

This creates a file listing all installed packages and their versions.

### 2. Install Dependencies from `requirements.txt`

For someone else (or on a new machine):

```bash
pip install -r requirements.txt
```
