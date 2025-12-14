# Hotel Booking API

REST API developed with **Python** and **Flask** as a study project, aiming to practice backend concepts such as authentication, database integration and RESTful architecture.

##  Technologies
- Python
- Flask
- Flask-RESTful
- Flask-JWT-Extended
- Flask-SQLAlchemy
- SQLite

##  Features
- User registration and authentication (JWT)
- Hotel CRUD (Create, Read, Update, Delete)
- Protected routes using JWT
- Token blacklist (logout)

##  How to run the project

```bash
# clone repository
git clone https://github.com/your-username/hotel-booking-api.git

# enter project folder
cd hotel-booking-api

# create virtual environment
python -m venv venv

# activate venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run application
python main.py