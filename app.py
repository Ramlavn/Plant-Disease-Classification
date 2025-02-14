import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Define the class labels and descriptions
class_labels = [
    'Pepper bell Bacterial spot',
    'Pepper bell healthy',
    'Potato Early_blight',
    'Potato Late_blight',
    'Potato healthy',
    'Tomato Bacterial spot',
    'Tomato Early_blight',
    'Tomato Late_blight',
    'Tomato Leaf_Mold',
    'Tomato Septoria leaf spot',
    'Tomato Spider mites Two spotted spider mite',
    'Tomato Target_Spot',
    'Tomato Tomato_YellowLeaf Curl_Virus',
    'Tomato Tomato mosaic virus',
    'Tomato healthy'
]

class_descriptions = {
    'Pepper bell Bacterial spot': 'A bacterial infection affecting pepper plants, causing dark, sunken lesions on leaves and fruits.',
    'Pepper bell healthy': 'The pepper plant is healthy with no visible signs of disease.',
    'Potato Early_blight': 'A fungal disease causing dark, concentric rings on potato leaves and stems.',
    'Potato Late_blight': 'A serious fungal infection that causes dark, water-soaked lesions on leaves and stems.',
    'Potato healthy': 'The potato plant is healthy with no visible signs of disease.',
    'Tomato Bacterial spot': 'A bacterial disease that causes dark spots with yellow halos on tomato leaves and fruits.',
    'Tomato Early_blight': 'A fungal disease causing dark spots with concentric rings on tomato leaves.',
    'Tomato Late_blight': 'A serious fungal disease causing large, irregular dark spots on tomato leaves and fruits.',
    'Tomato Leaf_Mold': 'A fungal disease causing grayish, moldy growth on the underside of tomato leaves.',
    'Tomato Septoria leaf spot': 'A fungal infection leading to small, round spots with dark edges on tomato leaves.',
    'Tomato Spider mites Two spotted spider mite': 'Pests that cause stippling and webbing on tomato leaves, leading to reduced plant vigor.',
    'Tomato Target_Spot': 'A fungal disease causing dark spots with concentric rings on tomato leaves and stems.',
    'Tomato Tomato_YellowLeaf Curl_Virus': 'A virus causing yellowing and curling of tomato leaves.',
    'Tomato Tomato mosaic virus': 'A virus causing mottled yellow and green patterns on tomato leaves and fruits.',
    'Tomato healthy': 'The tomato plant is healthy with no visible signs of disease.'
}

# Load your Keras model
model = load_model('my_model.h5')

# Function to preprocess the image
def preprocess_image(image, target_size):
    image = image.resize(target_size)
    image_array = np.array(image)
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    return image_array

# Streamlit app configuration
st.set_page_config(page_title="Plant Disease Classification", layout="wide")

# Streamlit app
st.title("Plant Disease Classification")

# Create a two-column layout
col1, col2 = st.columns([1, 2])

with col1:
    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])
    
with col2:
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        
        # Preprocess the image
        processed_image = preprocess_image(image, target_size=(256, 256))  # Change size based on your model
        
        # Make prediction
        prediction = model.predict(processed_image)
        
        # Get the predicted class label and confidence score
        predicted_class = np.argmax(prediction)
        predicted_label = class_labels[predicted_class]
        confidence_score = np.max(prediction)
        
        # Show prediction and confidence score
        st.write(f"The disease is predicted to be: {predicted_label}")
        st.write(f"Confidence score: {confidence_score:.2f}")
        
        # Show description of the predicted class
        st.write("Description:")
        st.write(class_descriptions.get(predicted_label, "No description available."))
    else:
        st.write("Upload an image to classify.")
