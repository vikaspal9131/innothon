# disease_info_page.py

import streamlit as st
from snomed_descriptions import snomed_descriptions

def display_disease_info():
    st.title("🦠 Disease Information")

    st.write(
        "📚 Browse through the detailed information of various diseases including symptoms, risk factors, treatment options, and more."
    )

    # Create a dropdown for users to select a disease
    disease_names = list(snomed_descriptions.keys())
    selected_disease = st.selectbox("Select a Disease", options=disease_names)

    if selected_disease:
        description = snomed_descriptions.get(selected_disease, {})

        st.subheader(f"🩺 {description.get('Condition Name', 'Unknown Disease')}")

        st.write(f"**📜 Description:** {description.get('Description', 'No description available.')}")
        st.write(f"**🩹 Symptoms/Clinical Presentation:** {', '.join(description.get('Symptoms/Clinical Presentation', []))}")
        st.write(f"**⚠️ Risk Factors:** {', '.join(description.get('Risk Factors', []))}")
        st.write(f"**❓ Possible Causes:** {', '.join(description.get('Possible Causes', []))}")
        st.write(f"**🩻 Diagnostic Criteria:** {', '.join(description.get('Diagnostic Criteria', []))}")

        # Formatting Treatment Options
        treatment_options = description.get('Treatment Options', {})
        if treatment_options:
            treatments = [f"{option}: {', '.join(details)}" for option, details in treatment_options.items()]
            st.write(f"**💊 Treatment Options:**\n{', '.join(treatments)}")
        else:
            st.write("**💊 Treatment Options:** No treatment information available.")

        st.write(f"**🔮 Prognosis:** {description.get('Prognosis', 'No prognosis information available.')}")
        st.write(f"**🛡️ Prevention:** {', '.join(description.get('Prevention', []))}")

        # Formatting Additional Resources
        additional_resources = description.get('Additional Resources', [])
        if additional_resources:
            resources = [f"[{resource['Title']}]({resource['Link']})" for resource in additional_resources]
            st.write(f"**📚 Additional Resources:** {', '.join(resources)}")
        else:
            st.write("**📚 Additional Resources:** No additional information available.")

        st.write(f"**📝 SNOMED Code:** `{selected_disease}`")
        st.write(f"**📑 Detailed Description:** {description.get('Detailed Description', 'No detailed description available.')}")
        st.write(f"**🔍 Clinical Findings:** {', '.join(description.get('Clinical Findings', []))}")
        st.write(f"**🧾 Associated Conditions:** {', '.join(description.get('Associated Conditions', []))}")
        st.write(f"**📋 Treatment Guidelines:** {', '.join(description.get('Treatment Guidelines', []))}")

if __name__ == "__main__":
    display_disease_info()
