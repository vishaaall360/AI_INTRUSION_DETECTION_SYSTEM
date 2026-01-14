# 🛡️ AI-Based Intrusion Detection System (IDS)

AI-Based Intrusion Detection System (IDS) is a cyber-security project that uses machine learning to analyze network traffic data and detect malicious activities. The system classifies traffic as normal or attack based on learned patterns, helping in early detection of potential intrusions and threats.

This project demonstrates the application of AI in defensive cyber security and is suitable as a strong GitHub portfolio and academic project.

---

## 🚀 Features

- Detects **normal vs malicious** network traffic
- Uses **machine learning (Random Forest)** for classification
- Analyzes traffic features such as duration, bytes transferred, and failed logins
- Displays results with **confidence score**
- Simple and interactive **Flask web dashboard**
- Modular and easy-to-extend codebase

---

## 🛠️ Tech Stack

- **Python 3.11**
- **Flask** – Web framework
- **Scikit-learn** – Machine learning
- **Pandas** – Data handling
- **Joblib** – Model saving/loading
- **HTML & CSS** – Frontend interface

---

## 📁 Project Structure

ai-intrusion-detection-system/
│
├── app.py
├── train_model.py
├── preprocess.py
├── predict.py
├── requirements.txt
│
├── data/
│ └── sample_logs.csv
│
├── model/
│ └── ids_model.pkl
│
├── templates/
│ └── dashboard.html
│
├── static/
│ └── style.css

1️⃣ Install Dependencies

pip install -r requirements.txt

2️⃣ Train the Machine Learning Model

python train_model.py

3️⃣ Start the Application

python app.py

4️⃣ Open in Browser

http://127.0.0.1:5000
