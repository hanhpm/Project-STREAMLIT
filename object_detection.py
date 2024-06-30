import cv2
import numpy as np
from PIL import Image
import streamlit as st

# Constants
MODEL_PATH = "model/MobileNetSSD_deploy.caffemodel"
PROTOTXT_PATH = "model/MobileNetSSD_deploy.prototxt.txt"
CONFIDENCE_THRESHOLD = 0.5
INPUT_IMAGE_DIM = (300, 300)
SCALE_FACTOR = 0.007843
MEAN_VALUE = 127.5

# Class labels used in the model
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus",
           "car", "cat", "chair", "cow", "diningtable", "dog", "horse",
           "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

def load_model(prototxt_path, model_path):
    """
    Load the Caffe model from disk.
    """
    return cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

def preprocess_image(image):
    """
    Preprocess the input image for the model.
    """
    resized_image = cv2.resize(image, INPUT_IMAGE_DIM)
    blob = cv2.dnn.blobFromImage(resized_image, SCALE_FACTOR, INPUT_IMAGE_DIM, MEAN_VALUE)
    return blob

def get_detections(net, image_blob):
    """
    Get detections from the model.
    """
    net.setInput(image_blob)
    return net.forward()

def draw_boxes(image, detections, confidence_threshold=CONFIDENCE_THRESHOLD):
    """
    Draw bounding boxes and class labels on the image based on the detections.
    """
    (h, w) = image.shape[:2]
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > confidence_threshold:
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (start_x, start_y, end_x, end_y) = box.astype("int")
            label = f"{CLASSES[idx]}: {confidence:.2f}"
            cv2.rectangle(image, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)
            y = start_y - 15 if start_y - 15 > 15 else start_y + 15
            cv2.putText(image, label, (start_x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return image

def main():
    """
    Main function to run Streamlit app.
    """
    st.title('Object Detection for Images')
    file = st.file_uploader('Upload Image', type=['jpg', 'png', 'jpeg'])
    
    if file is not None:
        st.image(file, caption="Uploaded Image")
        
        # Convert the file to an image
        image = Image.open(file)
        image = np.array(image)
        
        # Load model and process image
        net = load_model(PROTOTXT_PATH, MODEL_PATH)
        image_blob = preprocess_image(image)
        detections = get_detections(net, image_blob)
        
        # Annotate image and display result
        processed_image = draw_boxes(image, detections)
        st.image(processed_image, caption="Processed Image")

if __name__ == "__main__":
    main()