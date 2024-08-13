import os
import shutil
import streamlit as st
import time
from PIL import Image
from utils import load_custom_model, measure_memory_usage, find_duplicate_images, resize_image, save_and_extract_zip

def main():
    st.title("Image Deduplication")

    # Layout for placing the image in the top left corner
    col1, col2 = st.columns([1, 5])  # Adjust the ratio as needed
    with col1:
        st.image("image.jpg", use_column_width=True)  # Display the image without a caption
    with col2:
        st.write("")  # Leave the main column empty initially

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
            for group_index, group in enumerate(duplicates):
                cols = st.columns(len(group))  # One column per image
                for idx, (file, similarity) in enumerate(group):
                    with cols[idx]:
                        st.image(resize_image(Image.open(file), (150, 150)))
                        st.write(f"Similarity: {similarity:.2f}%")
                        st.write(file)

                st.write("--------")
            
            # Clean up temporary files
            shutil.rmtree(folder_path)
        else:
            st.write("Please upload a zip file.")

if __name__ == "__main__":
    main()
