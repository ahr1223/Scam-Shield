
# 🚨 ScamShield - AI-Based Scam Message & Call Detector

**ScamShield** is an AI-powered web application designed to detect scam messages and simulate scam call detection. Built using Flask and machine learning, it helps users identify fraudulent communication and protect themselves from cyber scams.

---

## 🧠 Features

- 📩 **Scam Message Detection** – Paste a message and get instant scam prediction.
- 📞 **Simulated Scam Call Detection** *(Coming Soon)* – Educates users through fake scam call interactions.
- 📱 **Mobile-Like Design** – Fully responsive layout that works like a mobile app.
- 🧠 **ML/NLP Based** – Uses a trained model with natural language processing for accuracy.
- ⚙️ **Lightweight Backend** – Built with Flask for fast and easy deployment.

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, pandas, pickle
- **Hosting/Deployment**: Localhost / Render / Heroku (optional)

---

## 📁 Project Structure

```
ScamShield/
├── static/              # CSS, JS, images
│   ├── css/
│   └── js/
│
├── templates/           # HTML pages
│   ├── index.html
│   └── result.html
│
├── model/               # Saved ML model files
│   ├── scam_model.pkl
│   └── vectorizer.pkl
│
├── app.py               # Main Flask app
├── requirements.txt     # Python packages
└── README.md            # This file
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ScamShield.git
cd ScamShield
```

### 2. Set up a virtual environment (optional but recommended)

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

## 🔮 Upcoming Features

- 🧠 Scam call voice simulation (Phase 2)
- 📱 Convert to Android app using WebView or PWA
- 📊 Add scam analytics and report dashboard
- 📤 Upload CSV or bulk check messages

---

## 🤖 Model Info

- NLP model trained on labeled text (scam / not scam)
- Uses `TfidfVectorizer` + Logistic Regression / Naive Bayes
- Saved using `pickle` for easy reuse in Flask

---

## 🧑‍💻 Developed By

**Harsh Vishwakarma**  
B.Tech CSE-AI | KIET 
Email: harshvishwakarma8805@gmail.com

---


> Built with ❤️ for the World's Largest Hackathon 2025 🌍
