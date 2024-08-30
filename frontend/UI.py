import streamlit as st
from snomed_descriptions import snomed_classes, snomed_descriptions
from ecg_utils import load_and_preprocess_ecg, diagnose_ecg, generate_ecg_report
import api_docs as api_docs
import disease_info_page as disease_info_page
import ecg_images_page as ecg_images_page
import faq_page as faq_page
import api_testing_page as api_testing_page

# Streamlit App
st.title("💓 ECG Signal Diagnosis")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Disease Information", "ECG Images", "API Documentation", "API Testing", "FAQ"])

if page == "Home":
    st.write(
        "🩺 Upload your ECG signal file (.mat) to get a comprehensive diagnosis and valuable insights."
    )

    # File uploader
    uploaded_file = st.file_uploader("📁 Choose your ECG file", type="mat")

    if uploaded_file is not None:
        # Display a message to the user
        st.success("✅ File uploaded successfully! Processing the data...")

        # Preprocess the file and make a diagnosis
        data = load_and_preprocess_ecg(uploaded_file)
        predicted_classes, predicted_probabilities = diagnose_ecg(data, snomed_classes)

        # Display the predictions
        st.subheader("🔍 Diagnosis Results:")

        if predicted_classes:
            for i, (cls, prob) in enumerate(zip(predicted_classes, predicted_probabilities)):
                description = snomed_descriptions.get(cls, {})

                st.markdown(f"### **🩺 Predicted Condition {i+1}:** `{description.get('Condition Name', 'Unknown Condition')}`")
                st.write(f"**🧬 Probability Score:** `{prob:.4f}`")
                st.write(f"**📜 Description:** {description.get('Description', 'No description available.')}")
                st.write(f"**🩹 Symptoms/Clinical Presentation:** {', '.join(description.get('Symptoms/Clinical Presentation', []))}")
                st.write(f"**⚠️ Risk Factors:** {', '.join(description.get('Risk Factors', []))}")
                st.write(f"**❓ Possible Causes:** {', '.join(description.get('Possible Causes', []))}")
                st.write(f"**🩻 Diagnostic Criteria:** {', '.join(description.get('Diagnostic Criteria', []))}")

                # Formatting Treatment Options
                treatment_options = description.get('Treatment Options', {})
                if treatment_options:
                    treatments = [f"**{option}:** {', '.join(details)}" for option, details in treatment_options.items()]
                    st.write(f"**💊 Treatment Options:**\n{', '.join(treatments)}")
                else:
                    st.warning("**💊 Treatment Options:** No treatment information available.")

                st.write(f"**🔮 Prognosis:** {description.get('Prognosis', 'No prognosis information available.')}")
                st.write(f"**🛡️ Prevention:** {', '.join(description.get('Prevention', []))}")

                # Formatting Additional Resources
                additional_resources = description.get('Additional Resources', [])
                if additional_resources:
                    resources = [f"[{resource['Title']}]({resource['Link']})" for resource in additional_resources]
                    st.write(f"**📚 Additional Resources:** {', '.join(resources)}")
                else:
                    st.info("**📚 Additional Resources:** No additional information available.")

                st.write(f"**📝 SNOMED Code:** `{cls}`")
                st.write(f"**📑 Detailed Description:** {description.get('Detailed Description', 'No detailed description available.')}")
                st.write(f"**🔍 Clinical Findings:** {', '.join(description.get('Clinical Findings', []))}")
                st.write(f"**🧾 Associated Conditions:** {', '.join(description.get('Associated Conditions', []))}")
                st.write(f"**📋 Treatment Guidelines:** {', '.join(description.get('Treatment Guidelines', []))}")

                st.markdown("---")

            # Generate PDF report
            pdf_buffer = generate_ecg_report(predicted_classes, predicted_probabilities, snomed_descriptions)

            # Download button
            st.download_button(
                label="Download ECG Report",
                data=pdf_buffer,
                file_name="ecg_diagnosis_report.pdf",
                mime="application/pdf"
            )

        else:
            st.error("🚫 No conditions detected with sufficient confidence.")

elif page == "Disease Information":
    disease_info_page.display_disease_info()

elif page == "ECG Images":
    ecg_images_page.display_ecg_images()

elif page == "API Documentation":
    api_docs.show_api_docs()

elif page == "API Testing":  # New API Testing page option
    api_testing_page.api_testing_page()
    
elif page == "FAQ":
    faq_page.display_faq()
