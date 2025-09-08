# 🧠 Sentiment Analysis Web App  

A simple and interactive **Django-based web application** that performs **sentiment analysis** on user-input text.  
It classifies the text into **Positive, Negative, or Neutral**, and also displays **polarity** and **subjectivity** scores using `TextBlob`.  

---

## 📌 Features  
- ✅ Classifies text as **Positive / Negative / Neutral**  
- ✅ Displays **polarity** and **subjectivity** scores  
- ✅ User-friendly web interface  
- ✅ Styled with CSS for better visuals  
- ✅ Built using **Django 5.2** and **TextBlob**  

---

## 📂 Project Structure  

```

sentiment\_app/
│── sentiment/                # App folder
│   ├── static/sentiment/     # CSS files
│   │   └── style.css
│   ├── templates/sentiment/  # HTML templates
│   │   ├── index.html
│   │   └── result.html
│   ├── urls.py               # App URL routing
│   └── views.py              # App views (logic)
│
│── SentimentProject/         # Main Django project folder
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
│── db.sqlite3                # SQLite database (auto-created)
│── manage.py                 # Django management file
│── requirements.txt          # Project dependencies
│── README.md                 # Project documentation

````

---

## ⚙️ Modules Used  

### Core Dependencies  
- **Django** – Web framework  
- **TextBlob** – NLP library for sentiment analysis  

### Supporting Modules  
- **pytz** – Timezone support (comes with Django)  

---

## 📥 Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/yourusername/sentiment-analysis-django.git
cd sentiment-analysis-django
````

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
source venv/bin/activate # On Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Start the Server

```bash
python manage.py runserver
```

Now open 👉 `http://127.0.0.1:8000/` in your browser.

---

## 🖥️ Usage

1. Enter a sentence or paragraph in the text box.
2. Click **Analyze**.
3. The app will display:

   * **Polarity** (range: `-1.0` = negative, `1.0` = positive)
   * **Subjectivity** (range: `0.0` = fact, `1.0` = opinion)
   * **Sentiment Classification** (Positive / Negative / Neutral)

---

## 📝 Example Inputs

* `"I love this project, it’s amazing!"` → **Positive**
* `"This is the worst experience ever."` → **Negative**
* `"I went to the store to buy milk."` → **Neutral**

---

## 🚀 Future Enhancements

* Add **charts & graphs** for visualization
* Provide **bulk text analysis** (upload files)
* Multi-language support for sentiment detection
* Integration with APIs (Twitter, Reddit, etc.)

---

## 📌 Requirements

All dependencies are listed in `requirements.txt`:

```txt
Django==5.2.6
textblob
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Feel free to fork this repo, raise issues, and submit pull requests!

---
