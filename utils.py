import os
import psutil
import zipfile
import shutil  # Add this line to import the shutil module
from PIL import Image
import numpy as np
from tensorflow.keras.applications import Xception
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing import image as keras_image
from tensorflow.keras.applications.xception import preprocess_input
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity

def resize_image(img, size):
    """Resize image to the given size."""
    return img.resize(size)

def convert_to_rgb(img):
    """Convert image to RGB mode."""
    return img.convert('RGB')

def preprocess_image(img, target_size):
    """Preprocess image for Xception model."""
    img = img.resize(target_size)
    img = keras_image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

def create_custom_xception_model():
    """Create a customized Xception model."""
    base_model = Xception(weights='imagenet', include_top=False, input_shape=(299, 299, 3))

    # Add custom layers
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(512, activation='relu')(x)
    x = Dense(256, activation='relu')(x)
    x = Dense(128, activation='relu')(x)
    
    # Output layer
    predictions = Dense(128, activation='relu')(x)

    # Create and return the model
    model = Model(inputs=base_model.input, outputs=predictions)
    return model

def load_custom_model():
    """Load the customized Xception model."""
    return create_custom_xception_model()

def measure_memory_usage():
    """Measure the current memory usage of the process."""
    process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss / 1024 / 1024  # in MB
    return memory_usage

def extract_features(img, model):
    """Extract features using the customized Xception model."""
    features = model.predict(img)
    return features

def find_duplicate_images(folder, model, target_size=(299, 299), threshold=0.85):
    """Find duplicate images in a folder based on feature similarity."""
    
    feature_list = []
    file_paths = []

    # Traverse the directory
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tif', '.tiff')):
                file_path = os.path.join(root, file)
                try:
                    with Image.open(file_path) as img:
                        rgb_img = convert_to_rgb(img)
                        preprocessed_img = preprocess_image(rgb_img, target_size)
                    img_features = extract_features(preprocessed_img, model).flatten()
                    
                    feature_list.append(img_features)
                    file_paths.append(file_path)

                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    # Check if feature_list is empty
    if not feature_list:
        print("No features extracted. Please check if the images are processed correctly.")
        return [], []

    # Convert feature_list to a NumPy array and print its shape
    feature_list = np.array(feature_list)

    # Reduce dimensionality
    pca = PCA(n_components=50)  # Reduce dimensions to 50 components
    reduced_features = pca.fit_transform(feature_list)

    # Calculate cosine similarity between feature vectors
    similarity_matrix = cosine_similarity(reduced_features)
    
    # Identify duplicates based on similarity
    duplicates = []
    visited = set()
    unique_images = set(file_paths)
    
    for i in range(len(file_paths)):
        if i in visited:
            continue
        group = [(file_paths[i], 100)]  # Each image is 100% similar to itself
        visited.add(i)
        for j in range(i + 1, len(file_paths)):
            if similarity_matrix[i, j] > threshold:
                similarity = similarity_matrix[i, j] * 100
                group.append((file_paths[j], similarity))
                visited.add(j)
                if file_paths[j] in unique_images:
                    unique_images.remove(file_paths[j])
        if len(group) > 1:
            duplicates.append(group)

    return duplicates, list(unique_images)

def save_and_extract_zip(uploaded_file):
    """Save and extract the uploaded zip file."""
    folder_path = "temp_images"
    os.makedirs(folder_path, exist_ok=True)
    
    zip_path = os.path.join(folder_path, uploaded_file.name)
    with open(zip_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(folder_path)
    
    return folder_path

def save_unique_images(unique_images, original_folder):
    """Save unique images maintaining the original folder structure."""
    unique_folder_path = "unique_images"
    if os.path.exists(unique_folder_path):
        shutil.rmtree(unique_folder_path)
    os.makedirs(unique_folder_path, exist_ok=True)
    
    for file_path in unique_images:
        relative_path = os.path.relpath(file_path, original_folder)
        destination = os.path.join(unique_folder_path, relative_path)
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        shutil.copy2(file_path, destination)
    
    return unique_folder_path
