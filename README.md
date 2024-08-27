<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI-Driven Solution for Managing Duplicate Images in Digital Archives</title>
</head>
<body>

<h1>AI-Driven Solution for Managing Duplicate Images in Digital Archives</h1>

<h2>Overview</h2>
<p>
    This project explores the development and implementation of an AI-driven solution to detect and manage duplicate images 
    within large-scale digital archives. Specifically, it focuses on the digitized collection of British Royal Naval ships 
    at the National Museum of the Royal Navy (NMRN). The project leverages advanced AI models—Perceptual Hashing (pHash), 
    Inception V3, and Xception—to address the challenges posed by the proliferation of duplicate digital assets.
</p>

<h2>Problem Statement</h2>
<p>
    In the digital era, institutions like museums and archives face the challenge of managing extensive digital archives. 
    One critical issue is the presence of duplicate images, which can complicate cataloging, retrieval, and storage management. 
    This project aims to develop a solution that can efficiently identify and manage these duplicates.
</p>

<h2>Approach</h2>

<h3>AI Models</h3>
<p>The project evaluates three AI models for detecting duplicate images:</p>
<ul>
    <li><strong>Perceptual Hashing (pHash):</strong> Analyzes the content of images to generate a unique fingerprint, facilitating the detection of duplicates.</li>
    <li><strong>Inception V3:</strong> A convolutional neural network that provides high accuracy in image classification tasks.</li>
    <li><strong>Xception:</strong> A deep learning model that enhances efficiency and accuracy in image recognition, known for its performance in handling image data.</li>
</ul>

<h3>Implementation</h3>
<p>A user-friendly interface was developed using Streamlit, allowing museum staff to:</p>
<ul>
    <li>Upload folders containing images.</li>
    <li>Detect duplicates using the selected AI model.</li>
    <li>Manage the digital archive by removing or merging duplicate assets.</li>
</ul>

<h3>Comparative Analysis</h3>
<p>The project includes a comparative analysis of the models, evaluating:</p>
<ul>
    <li><strong>Accuracy:</strong> How well each model identifies duplicate images.</li>
    <li><strong>Processing Time:</strong> The time taken by each model to analyze and process the images.</li>
    <li><strong>Memory Usage:</strong> The computational resources required by each model during operation.</li>
</ul>

<h2>Results</h2>
<p>
    <strong>Xception</strong> emerged as the recommended model due to its balanced performance across accuracy, processing time, 
    and memory usage. The AI-driven tool developed in this project significantly improves the efficiency of managing digital 
    archives, offering a scalable solution for the NMRN and potentially other institutions facing similar challenges.
</p>

<h2>Conclusion</h2>
<p>
    The implementation of this AI-driven solution represents a significant advancement in digital archive management. 
    It not only addresses a critical need within the NMRN but also provides a framework that can be adapted by other institutions 
    to handle duplicate digital assets effectively.
</p>

<h2>Usage</h2>
<p>To use the tool developed in this project:</p>
<ol>
    <li>Clone this repository.</li>
    <li>Install the required dependencies listed in <code>requirements.txt</code>.</li>
    <li>Run the Streamlit interface by executing the following command in your terminal:</li>
</ol>
<pre>
<code>streamlit run app.py</code>
</pre>
<ol start="4">
    <li>Upload your image folders through the interface, and the tool will automatically detect and manage duplicate images in your digital archive.</li>
</ol>

<h2>Dependencies</h2>
<ul>
    <li>Python 3.x</li>
    <li>Streamlit</li>
    <li>TensorFlow</li>
    <li>NumPy</li>
    <li>OpenCV</li>
    <li>scikit-image</li>
</ul>
<p>For detailed installation instructions, refer to the <code>requirements.txt</code> file.</p>

<h2>License</h2>
<p>
    This project is licensed under the MIT License. See the <code>LICENSE</code> file for more details.
</p>

<h2>Acknowledgments</h2>
<p>
    This project was conducted as part of a dissertation at the National Museum of the Royal Navy (NMRN). 
    Special thanks to the museum staff for their support and collaboration.
</p>

</body>
</html>
