# 🩺 Liver Cirrhosis Prediction Web App

A full-stack machine learning web application to **predict liver cirrhosis risk** based on 36 clinical features. The goal is to assist healthcare professionals and patients in the **early detection** of liver cirrhosis using a trained Random Forest model.

---

## 📌 Table of Contents

- [🔍 Problem Statement](#-problem-statement)
- [🎯 Project Objectives](#-project-objectives)
- [⚙️ Technologies Used](#-technologies-used)
- [🚀 Features](#-features)
- [📁 Folder Structure](#-folder-structure)
- [🛠️ Setup Instructions](#-setup-instructions)
- [🔐 Model & Normalizer](#-model--normalizer)
- [📡 API Route](#-api-route)
- [🖥️ UI Screens](#-ui-screens)
- [🔮 Future Scope](#-future-scope)
- [🤝 Contributions](#-contributions)
- [📄 License](#-license)

---

## 🔍 Problem Statement

Liver Cirrhosis is a chronic disease that causes irreversible damage to the liver and is often diagnosed too late. This project aims to predict whether a patient is **at risk of cirrhosis** using historical medical data and machine learning.

---

## 🎯 Project Objectives

- Predict liver cirrhosis based on user input data (clinical parameters).
- Deploy a lightweight, intuitive web app using Flask and HTML.
- Visualize results clearly for medical practitioners and patients.

---

## ⚙️ Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript  
- **Backend**: Python (Flask), Joblib  
- **ML Model**: Random Forest (Scikit-learn)  
- **Visualization**: Matplotlib, Seaborn (for training)  
- **Data Preprocessing**: Pandas, NumPy  
- **Deployment Ready**

---

## 🚀 Features

- 🔍 Accepts **36 medical input features**
- 🔁 Uses a **pre-trained Random Forest model**
- 📉 Normalizes data using **L1 Normalizer**
- 🧠 Makes real-time predictions
- ✅ Clear UI to show prediction results
- 🔙 Back navigation and retry support
- 📱 Fully responsive and mobile-friendly

---

## 📁 Folder Structure

Liver_Cirrhosis_Predictor/
│
├── Flask/
│ ├── templates/
│ │ ├── intro.html
│ │ ├── index.html
│ │ └── result.html
│ ├── static/
│ │ └── style.css
│ ├── app.py
│ ├── normalizer.pkl
│ └── rf_acc_68.pkl
│
├── Training/
│ └── model_trainin.ipynb


## 🛠️ Setup Instructions

### 📌 Prerequisites:
- Python 3.x
- VS Code or any IDE
- Install required packages:
pip install flask joblib numpy pandas scikit-learn


▶️ Run the App:
cd Flask
python app.py
Then open http://localhost:5000 in your browser.


🔐 Model & Normalizer
rf_acc_68.pkl: Trained Random Forest classifier (accuracy ~100%)

normalizer.pkl: Scikit-learn L1 Normalizer used to scale input features before prediction



📡 API Route
POST /predict
Accepts form data from HTML and returns:
  "prediction": 0 or 1,
  "message": "✅ Not suffering from cirrhosis" or "⚠️ Likely suffering from cirrhosis"

  
🖥️ UI Screens
✅ intro.html: Overview, prevention, and importance of detection

✍️ index.html: Form to enter 36 inputs

📊 result.html: Result display

🎨 Styled with style.css in /static


🔮 Future Scope
Add login and save prediction history

Generate downloadable PDF reports

Add multilingual support (Telugu, Hindi, etc.)

Display probability/confidence levels

Use SHAP for model explainability



🤝 Contributions
Feel free to fork this repo and raise a PR. Contributions are welcome for:

UI enhancements

Model improvements

Error handling

Deployment to cloud platforms


Output Screenshots:
![Screenshot 2025-06-28 140858](https://github.com/user-attachments/assets/e43e2ab7-7051-497e-855f-f5a6308e071b)
![Screenshot 2025-06-28 140946](https://github.com/user-attachments/assets/8c010264-ed6a-44ab-ab6a-83560a73d03d)
![Screenshot 2025-06-28 141120](https://github.com/user-attachments/assets/772eee7c-a95a-4ff9-975f-3a0a6d1f596c)

Video Demo Link :
https://drive.google.com/file/d/11jIoTQBYwb5ruxlaNGLmiwzT-TJo7HdL/view?usp=drivesdk





