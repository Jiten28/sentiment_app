1️⃣ Install Required Libraries
pip install django textblob
python -m textblob.download_corpora

2️⃣ Create Django Project
django-admin startproject SentimentProject
cd SentimentProject
python manage.py startapp sentiment

3️⃣ Project Structure
sentiment_app/
│
├── manage.py
├── SentimentProject/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── sentiment/
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── sentiment/
│   │       ├── index.html
│   │       └── result.html
│   └── static/
│       └── sentiment/
│           └── style.css


How to Run the Django App

Migrate database:

python manage.py migrate


Run the server:

python manage.py runserver


Open your browser at:

http://127.0.0.1:8000/


Enter text, click Analyze, and view sentiment with polarity & subjectivity.