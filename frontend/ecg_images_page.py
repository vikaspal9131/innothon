# ecg_images_page.py

import streamlit as st
import os

def display_ecg_images():
    st.title("📈 ECG Diagnoses Images")

    st.write(
        "🖼️ Browse through the images representing different types of ECG diagnoses. Each image corresponds to a specific diagnosis."
    )

    # Path to the images folder
    images_folder = "images"

    # List of image filenames
    image_filenames = [
        'AnteriorwallMI.jpg', 'AnterolateralMI.jpg', 'AnteroseptalMI.jpg',
        'AtrialFibrillation.jpg', 'AtrialFlutter.jpg', 'AtrialTachycardia.jpg',
        'AV-Block.jpg', 'EvolvedphaseMI.jpg', 'HighAV_Block.jpg',
        'InferiorWallMI.jpg', 'Infero-lateralMI.jpg', 'Ischemia.jpg',
        'JunctionalRhythm.jpg', 'LateralMI.jpg', 'Left Ventricular Hypertrophy.jpg',
        'LeftBranchBundleBlock.jpg', 'RightBranchBundleBlock.jpg', 'SinusBradycardia.jpg',
        'SinusTachycardia.jpg', 'SupraventricularEctopics.jpg', 'SupraventricularTachycardia.jpg',
        'VentricularEctopics.jpg', 'VentricularPrematureComplexes.jpg', 'WPWsyndrome.jpg'
    ]

    # Display images
    for image_file in image_filenames:
        image_path = os.path.join(images_folder, image_file)
        if os.path.exists(image_path):
            st.image(image_path, caption=image_file, use_column_width=True)
        else:
            st.warning(f"**Warning:** Image file `{image_file}` not found in the folder.")

if __name__ == "__main__":
    display_ecg_images()
