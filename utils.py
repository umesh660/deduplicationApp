import os
import shutil
import streamlit as st
import time
from PIL import Image
from utils import load_custom_model, measure_memory_usage, find_duplicate_images, resize_image, save_and_extract_zip

def delete_image(file_path):
    """Delete the specified image file."""
    if os.path.isfile(file_path):
        os.remove(file_path)

def main():
    st.title("Image Deduplication")

    uploaded_file = st.file_uploader("Upload a zip file containing images", type=['zip'])
    
    if st.button("Find Duplicates", key="find_duplicates_button"):
        if uploaded_file:
            # Save and extract zip file
            folder_path = save_and_extract_zip(uploaded_file)
            
            # Load the custom model
            model = load_custom_model()
            
            # Measure memory usage before processing
            memory_before = measure_memory_usage()
            
            start_time = time.time()
            
            # Process the images and find duplicates
            duplicates = find_duplicate_images(folder_path, model, threshold=0.85)
            
            end_time = time.time()
            elapsed_time = end_time - start_time
            
            # Measure memory usage after processing
            memory_after = measure_memory_usage()
            memory_used = memory_after - memory_before
            
            st.write(f"Time taken: {elapsed_time:.2f} seconds")
            st.write(f"Memory used: {memory_used:.2f} MB")

            st.write("Duplicate image pairs:")
            for group in duplicates:
                cols = st.columns(len(group) * 2)  # Two columns per image (image and delete button)
                for idx, (file, similarity) in enumerate(group):
                    with cols[idx * 2]:
                        st.image(resize_image(Image.open(file), (150, 150)), caption=f"Similarity: {similarity:.2f}%")
                        st.write(file)
                    with cols[idx * 2 + 1]:
                        if st.button("Delete", key=f"delete_{file}"):
                            delete_image(file)
                            st.experimental_rerun()  # Refresh the app to reflect changes

                st.write("--------")
            
            # Clean up temporary files
            shutil.rmtree(folder_path)
        else:
            st.write("Please upload a zip file.")

if __name__ == "__main__":
    main()
