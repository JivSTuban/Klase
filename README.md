# Klase

A learning management and online assessment system for academic education.

## Features

- User Authentication and Authorization
- Course Management
  - Create and manage courses
  - Assign teachers and students
  - Course materials upload/download
- Assessment System
  - Multiple question types (MCQ, Essay, etc.)
  - Automated grading
  - Progress tracking
- Real-time Analytics
  - Student performance metrics
  - Course completion rates
  - Engagement statistics

## Tech Stack

1. Django - Backend framework
2. Bootstrap - Frontend styling
3. jQuery - Frontend interactivity
4. Chart.js - Data visualization
5. Animate.css - UI animations

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Git

## Run Locally

1. Clone the project
```bash
git clone https://github.com/JivSTuban/lms.git
```

2. Go to the project directory
```bash
git clone https://github.com/JivSTuban/lms.git
```

3. Create and activate virtual environment

For Windows:
```bash
python -m venv env
env\Scripts\activate
```

For macOS/Linux:
```bash
python -m venv env
source env/bin/activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Make migrations and migrate
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create admin/superuser
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver
```
The application will be available at http://127.0.0.1:8000/

Contributing
Fork the project
Create your feature branch
 ```bash
git checkout -b feature/AmazingFeature
```
Commit your changes
 ```bash
git commit -m 'Add some AmazingFeature'
```
Push to the branch
 ```bash
git push origin feature/AmazingFeature
```
Open a Pull Request