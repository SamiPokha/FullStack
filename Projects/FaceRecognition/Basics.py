import cv2
import numpy as np
import face_recognition


# Import image
imgElon = face_recognition.load_image_file('ImagesBasic/Elon Musk.jpg')
imgTest = face_recognition.load_image_file('ImagesBasic/Elon Test.jpg')

# Convert into RGB
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

# Display
cv2.imshow('Elon Musk',imgElon)
cv2.imshow('Elon Test',imgTest)
cv2.waitKey(0)
