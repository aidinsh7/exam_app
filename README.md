# Online Exam System

This project is an online exam system built with Django and Django Rest Framework (DRF). Users can take exams online and receive their results in the form of a report card. The project leverages various technologies to provide a smooth and efficient user experience.

## Technologies Used

- **Django**: `~=4.2.1`
- **Django Rest Framework**: `~=3.14.0`
- **Django REST Framework Simple JWT**: `~=5.2.2`
- **Kavenegar**: `~=1.1.2` (for SMS notifications)
- **Pillow**: `~=9.5.0` (for image processing)
- **psycopg2-binary**: `~=2.9.6` (PostgreSQL database adapter)
- **Celery**: `~=5.4.0` (for asynchronous task management)
- **Django Celery Beat**: `~=2.6.0` (for scheduling periodic tasks)
- **Django Celery Results**: `~=2.5.1` (to store the results of Celery tasks)
- **Django Redis**: `~=5.4.0` (for caching with Redis)
- **Firebase Admin SDK**: `~=6.5.0` (for various Firebase services)



## Installation

To get started with the project, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <project-directory>


2. **Create and Activate a Virtual Environment:**

   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`


3. **Install the Requirements:**

   pip install -r requirements.txt


4. **Set Up the Database:**

   Update settings.py with your PostgreSQL database credentials.
   Run migrations:
   python manage.py migrate


5. **Start the Redis Server:**
   Make sure you have Redis installed and started.


6. **Run the Celery Worker:**

   celery -A <project-name> worker -l info

7. **Run the Development Server:**
    python manage.py runserver