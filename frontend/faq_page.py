# faq_page.py

import streamlit as st

def display_faq():
    st.title("📚 Frequently Asked Questions (FAQ)")

    st.write(
        """
        **Welcome to the FAQ page!** Here you will find detailed answers to common questions about the ECG Signal Diagnosis app. This section covers everything from the deep learning model to how to use the app effectively.

        ### 1. What is the purpose of this app?

        This app is designed to analyze ECG signal files and provide diagnostic insights based on a trained deep learning model. It helps identify various heart conditions from ECG data and provides valuable information for medical professionals and researchers.

        ### 2. How does the deep learning model work?

        The deep learning model is trained on a large dataset of ECG signals to detect patterns associated with different heart conditions. It uses sophisticated neural network algorithms to classify ECG signals into various diagnostic categories.

        ### 3. What types of diagnoses can the app identify?

        The app can identify a range of conditions including:
        - Myocardial Infarction (MI) in different regions (e.g., Anterior, Inferior, etc.)
        - Atrial Fibrillation
        - Atrial Flutter
        - Various types of heart blocks
        - Ventricular Ectopics
        - And more...

        ### 4. How do I use the app?

        - **Upload an ECG File**: Click on the file uploader to choose your `.mat` ECG file.
        - **View Results**: After processing, the app will display diagnostic results including condition names, probabilities, and related information.
        - **Download Report**: Click the download button to get a detailed PDF report of your diagnosis.

        ### 5. What should I do if I encounter issues?

        - **Check File Format**: Ensure that your ECG file is in `.mat` format.
        - **File Size**: Verify that the file size is within acceptable limits.
        - **Contact Support**: If you need further assistance, please reach out through the contact form on our website or email support@example.com.

        ### 6. Where can I find more information about the project?

        The project provides a comprehensive ECG analysis tool designed for medical professionals and researchers. For more details, including technical specifications and research papers, visit our project page [here](https://example.com).

        ### 7. How can I contribute to the project?

        Contributions are welcome! You can contribute by providing feedback, reporting bugs, or even contributing code. For more information, visit our GitHub repository [here](https://github.com/your-repo).

        ### 8. Is there any documentation available?

        Yes, detailed documentation is available. You can find it on our [documentation page](https://example.com/docs).

        ### 9. How do I stay updated with the latest changes?

        Follow us on social media or subscribe to our newsletter for updates on new features and improvements.

        ### 10. What kind of ECG data is required?

        The app requires ECG data in `.mat` format with a specific structure. Ensure that your file contains the necessary data fields for accurate analysis.

        ### 11. How accurate is the diagnosis provided by the app?

        The accuracy of the diagnosis depends on the quality and completeness of the ECG data as well as the performance of the underlying deep learning model. The model is trained on a diverse dataset to provide reliable predictions, but it's always recommended to consult with a healthcare professional for medical decisions.

        ### 12. Can the app analyze ECG signals from different leads?

        Yes, the app can analyze ECG signals from different leads, provided they are included in the `.mat` file in the expected format.

        ### 13. What are the system requirements for running this app?

        The app can be run on any system that supports a modern web browser. It does not have specific hardware requirements but requires a stable internet connection for file uploads and processing.

        ### 14. How often is the deep learning model updated?

        The deep learning model is updated periodically based on new research and improved datasets. We strive to keep the model current with the latest advancements in ECG diagnostics.

        ### 15. Can I use this app for clinical purposes?

        While the app provides valuable diagnostic insights, it is not intended to replace professional medical advice. Always consult with a healthcare provider for clinical decisions.

        ### 16. How can I provide feedback on the app?

        Feedback is highly appreciated! You can provide feedback through our contact form on the website or by submitting issues on our GitHub repository [here](https://github.com/your-repo/issues).

        ### 17. Are there any privacy concerns with using the app?

        We take privacy seriously and ensure that your data is processed securely. The app does not store any personal information and complies with data protection regulations.

        ### 18. What should I do if the app does not recognize my file?

        If the app does not recognize your file, check that it is in the correct `.mat` format and that it follows the expected structure. If issues persist, contact support for assistance.

        ### 19. Can I integrate the app with other systems or tools?

        The app is designed to be a standalone tool, but we are open to integration requests. Contact us if you have specific integration needs.

        ### 20. What are the next steps for using the insights from the app?

        Use the diagnostic insights as a starting point for further medical evaluation. Discuss the results with a healthcare provider to determine the appropriate course of action.

        ### 21. How do I get started with using the app?

        Simply upload your ECG file, view the results, and download the report. For detailed instructions, refer to the user guide available on our [documentation page](https://example.com/docs).
        """
    )
