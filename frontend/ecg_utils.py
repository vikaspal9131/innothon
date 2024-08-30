# ecg_utils.py

import numpy as np
from keras.models import load_model
from scipy.io import loadmat
from keras.preprocessing.sequence import pad_sequences
from fpdf import FPDF
import io

# Load the pre-trained model
model = load_model('model/ecg_E10.h5')

def load_and_preprocess_ecg(file):
    """Function to load and preprocess the uploaded ECG file"""
    # Load the .mat file
    x = loadmat(file)
    data = np.asarray(x['val'], dtype=np.float64)

    # Pad the sequence to ensure it has the correct length
    data = pad_sequences(data, maxlen=5000, truncating='post', padding="post")
    data = data.reshape(1, 5000, 12)  # Reshape for model input
    return data

def diagnose_ecg(data, snomed_classes, threshold=0.5):
    """Function to make predictions"""
    # Make predictions using the model
    predictions = model.predict(data)
    
    # Identify classes with probabilities above the threshold
    predicted_indices = np.where(predictions[0] > threshold)[0]
    predicted_classes = snomed_classes[predicted_indices - 1]
    predicted_probabilities = predictions[0][predicted_indices]
    
    return predicted_classes, predicted_probabilities



def generate_ecg_report(predicted_classes, predicted_probabilities, snomed_descriptions):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="ECG Signal Diagnosis Report", ln=True, align='C')
    pdf.ln(10)

    if predicted_classes:
        for i, (cls, prob) in enumerate(zip(predicted_classes, predicted_probabilities)):
            description = snomed_descriptions.get(cls, {})

            pdf.set_font("Arial", size=10)
            pdf.cell(200, 10, txt=f"Predicted Condition {i+1}: {description.get('Condition Name', 'Unknown Condition')}", ln=True)
            pdf.cell(200, 10, txt=f"Probability Score: {prob:.4f}", ln=True)
            pdf.cell(200, 10, txt=f"Description: {description.get('Description', 'No description available.')}", ln=True)
            pdf.cell(200, 10, txt=f"Symptoms/Clinical Presentation: {', '.join(description.get('Symptoms/Clinical Presentation', []))}", ln=True)
            pdf.cell(200, 10, txt=f"Risk Factors: {', '.join(description.get('Risk Factors', []))}", ln=True)
            pdf.cell(200, 10, txt=f"Possible Causes: {', '.join(description.get('Possible Causes', []))}", ln=True)
            pdf.cell(200, 10, txt=f"Diagnostic Criteria: {', '.join(description.get('Diagnostic Criteria', []))}", ln=True)
            
            treatment_options = description.get('Treatment Options', {})
            if treatment_options:
                treatments = [f"{option}: {', '.join(details)}" for option, details in treatment_options.items()]
                pdf.cell(200, 10, txt=f"Treatment Options: {', '.join(treatments)}", ln=True)
            else:
                pdf.cell(200, 10, txt="Treatment Options: No treatment information available.", ln=True)

            pdf.cell(200, 10, txt=f"Prognosis: {description.get('Prognosis', 'No prognosis information available.')}", ln=True)
            pdf.cell(200, 10, txt=f"Prevention: {', '.join(description.get('Prevention', []))}", ln=True)

            additional_resources = description.get('Additional Resources', [])
            if additional_resources:
                resources = [f"{resource['Title']}: {resource['Link']}" for resource in additional_resources]
                pdf.cell(200, 10, txt=f"Additional Resources: {', '.join(resources)}", ln=True)
            else:
                pdf.cell(200, 10, txt="Additional Resources: No additional information available.", ln=True)

            pdf.cell(200, 10, txt=f"SNOMED Code: {cls}", ln=True)
            pdf.cell(200, 10, txt=f"Detailed Description: {description.get('Detailed Description', 'No detailed description available.')}", ln=True)
            pdf.cell(200, 10, txt=f"Clinical Findings: {', '.join(description.get('Clinical Findings', []))}", ln=True)
            pdf.cell(200, 10, txt=f"Associated Conditions: {', '.join(description.get('Associated Conditions', []))}", ln=True)
            pdf.cell(200, 10, txt=f"Treatment Guidelines: {', '.join(description.get('Treatment Guidelines', []))}", ln=True)

            pdf.ln(10)

    else:
        pdf.cell(200, 10, txt="No conditions detected with sufficient confidence.", ln=True)

    # Save PDF to a bytes buffer
    buffer = io.BytesIO()
    pdf.output(dest='S')  # Save PDF to a string (default)
    buffer.write(pdf.output(dest='S').encode('latin1'))
    buffer.seek(0)
    return buffer
