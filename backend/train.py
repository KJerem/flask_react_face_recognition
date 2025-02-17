import os
import numpy as np
from PIL import Image
import cv2
import pickle

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "data")

# Load the OpenCV face recognition detector Haar
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
if face_cascade.empty():
    raise Exception("Error loading Haar cascade. Check the path and file existence.")

# Create OpenCV LBPH recognizer for training
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
label_ids = {}
y_label = []
x_train = []

# Traverse all face images in `data` folder
for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace("", "").upper()  # name
            print(f"Processing file: {file}, Label: {label}")

            if label not in label_ids:
                label_ids[label] = current_id
                current_id += 1
            id_ = label_ids[label]
            print(f"Label IDs: {label_ids}")

            pil_image = Image.open(path).convert("L")
            image_array = np.array(pil_image, "uint8")
            print(f"Image array shape: {image_array.shape}")

            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

            if len(faces) == 0:
                print(f"No faces detected in {file}")
            else:
                for (x, y, w, h) in faces:
                    roi = image_array[y:y+h, x:x+w]
                    x_train.append(roi)
                    y_label.append(id_)
                    print(f"Detected face for label {label} at {file}")

# Check if we have enough training data
print(f"Total faces detected: {len(x_train)}")
print(f"Labels: {y_label}")

if len(x_train) < 2:
    raise Exception("Not enough training data. Need at least 2 faces.")

# Save the label ids to a file
with open("labels.pickle", "wb") as f:
    pickle.dump(label_ids, f)

# Train the recognizer and save the trained model
recognizer.train(x_train, np.array(y_label))
recognizer.save("train.yml")

print("Training completed successfully.")


# '''
# Project Description: A Fullstack application using Flask as backend, React as Frontend and MySQL as Database
# File Description: This file trains the data set for face recognition.

# '''
# import os
# import numpy as np
# from PIL import Image
# import cv2
# import pickle

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# image_dir = os.path.join(BASE_DIR, "data")

# # Load the OpenCV face recognition detector Haar
# face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
# # Create OpenCV LBPH recognizer for training
# recognizer = cv2.face.LBPHFaceRecognizer_create()

# current_id = 0
# label_ids = {}
# y_label = []
# x_train = []

# # Traverse all face images in `data` folder
# for root, dirs, files in os.walk(image_dir):
#     for file in files:
#         if file.endswith("png") or file.endswith("jpg"):
#             path = os.path.join(root, file)
#             label = os.path.basename(root).replace("", "").upper()  # name
#             print(label, path)

#             if label in label_ids:
#                 pass
#             else:
#                 label_ids[label] = current_id
#                 current_id += 1
#             id_ = label_ids[label]
#             print(label_ids)

#             pil_image = Image.open(path).convert("L")
#             image_array = np.array(pil_image, "uint8")
#             print(image_array)
#             # Using multiscle detection
#             faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

#             for (x, y, w, h) in faces:
#                 roi = image_array[y:y+h, x:x+w]
#                 x_train.append(roi)
#                 y_label.append(id_)

# # labels.pickle store the dict of labels.
# # {name: id}  
# # id starts from 0
# with open("labels.pickle", "wb") as f:
#     pickle.dump(label_ids, f)

# # Train the recognizer and save the trained model.
# recognizer.train(x_train, np.array(y_label))
# recognizer.save("train.yml")