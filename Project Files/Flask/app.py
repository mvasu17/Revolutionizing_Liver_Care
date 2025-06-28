from flask import Flask, render_template, request
import numpy as np
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model and normalizer
model = joblib.load('Flask/rf_acc_68.pkl')              # Your trained ML model
normalizer = joblib.load('Flask/normalizer.pkl')    # Your L1 normalizer

# List of input features in exact order
feature_names = [
    'Age', 'Gender', 'Duration of alcohol consumption(years)',
    'Quantity of alcohol consumption (quarters/day)', 'Hepatitis B infection',
    'Hepatitis C infection', 'Diabetes Result', 'Obesity',
    'Family history of cirrhosis/ hereditary', 'TCH', 'TG', 'LDL', 'HDL',
    'Hemoglobin  (g/dl)', 'PCV  (%)', 
    'MCV   (femtoliters/cell)', 
    'Total Count', 'Polymorphs  (%)', 'Lymphocytes  (%)', 'Monocytes   (%)',
    'Eosinophils   (%)', 'Basophils  (%)', 'Platelet Count  (lakhs/mm)',
    'Total Bilirubin    (mg/dl)', 'Direct    (mg/dl)', 'Indirect     (mg/dl)',
    'Total Protein     (g/dl)', 'Albumin   (g/dl)', 'Globulin  (g/dl)', 'A/G Ratio',
    'AL.Phosphatase      (U/L)', 'SGOT/AST      (U/L)', 'SGPT/ALT (U/L)',
    'USG Abdomen (diffuse liver or  not)',
     'BP_Systolic', 'BP_Diastolic'
]

@app.route('/')
def intro():
    return render_template('intro.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Read and preprocess input values
        input_values = []
        for feature in feature_names:
            value = request.form.get(feature)
            if value is None or value.strip() == '':
                value = 0  # default for missing
            input_values.append(float(value))

        # Convert to NumPy array and normalize
        input_array = np.array([input_values])
        input_normalized = normalizer.transform(input_array)

        # Predict using the loaded model
        prediction = model.predict(input_normalized)[0]

        # Convert prediction to readable message
        result_text = "✅ The patient is likely **NOT** suffering from Liver Cirrhosis." if prediction == 0 else "⚠️ The patient is likely **suffering** from Liver Cirrhosis. Please consult a specialist."

        return render_template('result.html', prediction=result_text)

    except Exception as e:
        return f"<h3>Error occurred: {e}</h3>"

if __name__ == '__main__':
    app.run(debug=True)