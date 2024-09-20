**Getting Started**

Before you begin, ensure you have the following prerequisites installed:

Python 3.12
Docker

Step 1 :
  Clone this repo git clone https://github.com/OnyenaucheyaEmmanuel/CowryWise-Test.git
        cd CowryWise-Test
  Create a Virtual Environment python -m venv venv
  Activate the Virtual Environment . venv/scripts/activate
  Install the dependencies pip install -r requirements.txt
  Make Migrations python manage.py makemigrations
  Migrate python manage.py migrate

Step 2 (Using Docker) :
  Clone this repo git clone https://github.com/OnyenaucheyaEmmanuel/CowryWise-Test.git
        cd CowryWise-Test
  Build and Run with Docker Compose   docker-compose up --build 
  Once Docker Compose finishes building and running the services, they can access the Django application by visiting: http://localhost:8000
